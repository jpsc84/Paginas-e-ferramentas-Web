// Trilha do Oeste: motor de navegação (rota, posição na rota, manobras e falas).
// Sem dependências; funciona no navegador (window.Nav) e no Node (module.exports) para testes.
(function (root) {
  'use strict';
  const R = 6371008.8, D2R = Math.PI / 180;

  // ---------- Geometria ([lon, lat]) ----------
  function hav(a, b) {
    const dLat = (b[1] - a[1]) * D2R, dLon = (b[0] - a[0]) * D2R;
    const s = Math.sin(dLat / 2) ** 2 + Math.cos(a[1] * D2R) * Math.cos(b[1] * D2R) * Math.sin(dLon / 2) ** 2;
    return 2 * R * Math.asin(Math.min(1, Math.sqrt(s)));
  }
  function bearing(a, b) {
    const f1 = a[1] * D2R, f2 = b[1] * D2R, dl = (b[0] - a[0]) * D2R;
    const y = Math.sin(dl) * Math.cos(f2);
    const x = Math.cos(f1) * Math.sin(f2) - Math.sin(f1) * Math.cos(f2) * Math.cos(dl);
    return (Math.atan2(y, x) / D2R + 360) % 360;
  }
  function lerp(a, b, t) { return [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t]; }
  // Projeta p no segmento a-b em plano local (metros). Retorna fração t e distância lateral d.
  function projSeg(p, a, b) {
    const kx = Math.cos(p[1] * D2R) * 111320, ky = 110574;
    const ax = (a[0] - p[0]) * kx, ay = (a[1] - p[1]) * ky;
    const bx = (b[0] - p[0]) * kx, by = (b[1] - p[1]) * ky;
    const dx = bx - ax, dy = by - ay, L2 = dx * dx + dy * dy;
    let t = L2 > 0 ? -(ax * dx + ay * dy) / L2 : 0;
    t = Math.max(0, Math.min(1, t));
    return { t, d: Math.hypot(ax + t * dx, ay + t * dy) };
  }
  const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));

  // ---------- Rota ----------
  // Converte a rota do OSRM (geometries=geojson, steps=true, overview=full) no formato interno.
  function buildRoute(r) {
    const c = r.geometry.coordinates;
    const cum = [0];
    for (let i = 1; i < c.length; i++) cum.push(cum[i - 1] + hav(c[i - 1], c[i]));
    const steps = [];
    let idx = 0;
    r.legs.forEach(leg => leg.steps.forEach(s => {
      const loc = s.maneuver.location;
      let best = idx, bd = Infinity;
      for (let i = idx; i < c.length; i++) {
        const d = hav(c[i], loc);
        if (d < bd) { bd = d; best = i; }
        if (d < 1) break;
      }
      idx = best;
      steps.push({
        type: s.maneuver.type, modifier: s.maneuver.modifier || '', exit: s.maneuver.exit || null,
        name: s.name || '', ref: s.ref || '', along: cum[best], distance: s.distance
      });
    }));
    return { coords: c, cum, total: cum[cum.length - 1], duration: r.duration, distance: r.distance, steps };
  }

  // Posição projetada na rota. hint = segmento da última posição válida (evita "pular" para trechos sobrepostos).
  function snap(rt, p, hint) {
    const c = rt.coords, n = c.length, cum = rt.cum;
    const scan = (i0, i1) => {
      let best = null;
      for (let i = i0; i < i1; i++) {
        const pr = projSeg(p, c[i], c[i + 1]);
        if (!best || pr.d < best.d) best = { i, t: pr.t, d: pr.d };
      }
      return best;
    };
    const h = clamp(hint || 0, 0, n - 2);
    let back = h; while (back > 0 && cum[h] - cum[back] < 60) back--;
    let fwd = h; while (fwd < n - 1 && cum[fwd] - cum[h] < 600) fwd++;
    let b = scan(back, Math.max(back + 1, fwd));
    if (!b || b.d > 40) {
      const g = scan(0, n - 1);
      if (g && (!b || g.d < b.d - 5)) b = g;
    }
    const along = cum[b.i] + b.t * (cum[b.i + 1] - cum[b.i]);
    return { seg: b.i, along, cross: b.d, bearing: bearing(c[b.i], c[b.i + 1]), point: lerp(c[b.i], c[b.i + 1], b.t) };
  }

  // Ponto e direção a uma distância "along" do início (usado no modo simulação).
  function pointAt(rt, along) {
    const c = rt.coords, cum = rt.cum, n = c.length;
    along = clamp(along, 0, rt.total);
    let lo = 0, hi = n - 2;
    while (lo < hi) { const m = (lo + hi + 1) >> 1; if (cum[m] <= along) lo = m; else hi = m - 1; }
    const L = cum[lo + 1] - cum[lo];
    const t = L > 0 ? (along - cum[lo]) / L : 0;
    return { point: lerp(c[lo], c[lo + 1], t), bearing: bearing(c[lo], c[lo + 1]), seg: lo };
  }

  // ---------- Textos ----------
  const ORD = ['primeira', 'segunda', 'terceira', 'quarta', 'quinta', 'sexta', 'sétima', 'oitava', 'nona', 'décima'];

  function sideOf(m) { return m.includes('right') ? 'direita' : m.includes('left') ? 'esquerda' : null; }

  // Manobras que não pedem ação do motorista (só troca de nome da via seguindo reto).
  function silent(st) {
    if (st.type === 'depart') return true;
    const m = st.modifier;
    return (st.type === 'new name' || st.type === 'continue' || st.type === 'notification') && (!m || m === 'straight');
  }

  function action(st, forSpeech) {
    const m = st.modifier, side = sideOf(m);
    switch (st.type) {
      case 'merge': return side ? `entre na via pela ${side}` : 'entre na via';
      case 'on ramp': return side ? `pegue o acesso à ${side}` : 'pegue o acesso';
      case 'off ramp': return side ? `pegue a saída à ${side}` : 'pegue a saída';
      case 'fork': return side ? `na bifurcação, mantenha-se à ${side}` : 'na bifurcação, siga em frente';
      case 'roundabout': case 'rotary':
        if (!st.exit) return 'entre na rotatória';
        return forSpeech && st.exit <= ORD.length
          ? `na rotatória, pegue a ${ORD[st.exit - 1]} saída`
          : `na rotatória, pegue a ${st.exit}ª saída`;
      case 'exit roundabout': case 'exit rotary': return 'saia da rotatória';
      case 'arrive': return 'chegada ao destino';
      default:
        if (m === 'uturn') return 'faça o retorno';
        if (!side || m === 'straight') return 'siga em frente';
        if (m.startsWith('sharp')) return `faça a curva fechada à ${side}`;
        if (m.startsWith('slight')) return `mantenha-se à ${side}`;
        return (st.type === 'continue' || st.type === 'new name') ? `continue à ${side}` : `vire à ${side}`;
    }
  }

  function roadOf(st) { return (st.name || st.ref || '').trim(); }

  // "na Rua X", "no Viaduto Y", "em Z"
  function withArticle(name) {
    if (!name) return '';
    if (/^(viaduto|largo|beco|anel|t[úu]nel|acesso|contorno|elevado|corredor|boulevard|parque|caminho|ramal|trevo|retorno|complexo|cais)(?![a-zà-ú])/i.test(name)) return 'no ' + name;
    if (/^((rua|avenida|av|rodovia|rod|estrada|travessa|tv|alameda|al|pra[çc]a|ponte|via|ladeira|marginal|vila|quadra|passarela|servid[ãa]o|ruela|r)(?![a-zà-ú])|[a-z]{2}-\s?\d)/i.test(name)) return 'na ' + name;
    return 'em ' + name;
  }

  const cap = s => s ? s[0].toUpperCase() + s.slice(1) : s;

  function screenDist(m) {
    if (m < 100) return Math.max(0, Math.round(m / 10) * 10) + ' m';
    if (m < 1000) return Math.round(m / 50) * 50 + ' m';
    if (m < 10000) return (Math.round(m / 100) / 10).toFixed(1).replace('.', ',') + ' km';
    return Math.round(m / 1000) + ' km';
  }
  function speechDist(m) {
    if (m < 1000) {
      const v = m < 200 ? Math.round(m / 10) * 10 : Math.round(m / 50) * 50;
      return v >= 1000 ? '1 quilômetro' : v + ' metros';
    }
    const km = Math.round(m / 100) / 10;
    if (km === 1) return '1 quilômetro';
    return (Number.isInteger(km) ? String(km) : km.toFixed(1).replace('.', ',')) + ' quilômetros';
  }

  // Instrução para a tela: { action: 'Vire à direita', road: 'Av. Frei Serafim' }
  function screenText(st) {
    if (st.type === 'arrive') return { action: 'Destino à vista', road: '' };
    return { action: cap(action(st, false)), road: roadOf(st) };
  }

  // ---------- Falas ----------
  // Cada fala é montada em trechos ("chunks"). O texto completo (com nomes de rua) vai para a voz do aparelho;
  // os trechos, sem nomes de rua, viram arquivos de áudio pré-gravados da voz do pistoleiro.
  // Tom formal, com um leve toque de faroeste só na palavra "trilha".
  const LEADS = ['Em {d},'];
  const FIXED = {
    depart: ['Rota traçada. Boa viagem.'],
    arrive: ['Destino alcançado. Fim da trilha.'],
    reroute: ['Desviamos da trilha. Recalculando.']
  };
  const CHAIN = 'E logo depois,', ARRIVE_TAIL = 'chegamos ao destino.';
  const lastPick = {};
  function rnd(kind, n) {
    let i = Math.floor(Math.random() * n);
    if (n > 1 && i === lastPick[kind]) i = (i + 1) % n;
    lastPick[kind] = i;
    return i;
  }
  // Distância falada em trechos longos, arredondada para caber num conjunto fechado de gravações.
  function contDist(m) {
    const km = m / 1000;
    let v;
    if (km < 10) v = Math.max(2, Math.round(km * 2) / 2);
    else if (km < 30) v = Math.round(km);
    else if (km < 100) v = Math.round(km / 5) * 5;
    else if (km < 300) v = Math.round(km / 10) * 10;
    else if (km < 1000) v = Math.round(km / 50) * 50;
    else return 'muitos quilômetros';
    return (Number.isInteger(v) ? String(v) : String(v).replace('.', ',')) + ' quilômetros';
  }
  function slug(t) {
    return t.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  }
  function Utt() { this.text = ''; this.chunks = []; }
  Utt.prototype.add = function (chunk, text) {
    this.chunks.push(slug(chunk));
    this.text += (this.text ? ' ' : '') + (text || chunk);
    return this;
  };
  function streetPart(st, a) {
    const road = roadOf(st);
    // Em rotatória e bifurcação o nome da via soa confuso; fala só a ação.
    return !road || /rotat|bifurca/.test(a) ? '' : ' ' + withArticle(road);
  }
  function addFar(u, st, dist) {
    const i = rnd('lead', LEADS.length);
    u.add(LEADS[i].replace('{d}', speechDist(dist)));
    if (st.type === 'arrive') { u.add(ARRIVE_TAIL); return u; }
    const a = action(st, true);
    return u.add(a + '.', a + streetPart(st, a) + '.');
  }
  function addNear(u, st) {
    const a = action(st, true);
    // "Na rotatória, pegue a segunda saída agora" soa estranho; nesses casos fala só a ação.
    return u.add(cap(a) + (/rotat|bifurca/.test(a) ? '.' : ' agora.'));
  }
  function addFixed(u, kind) { return u.add(FIXED[kind][rnd(kind, FIXED[kind].length)]); }
  function addCont(u, dist) { return u.add('Siga pela trilha por ' + contDist(dist) + '.'); }

  // Lista de todos os trechos possíveis (usada para gerar os arquivos de áudio).
  function allChunks() {
    const set = new Set([CHAIN, ARRIVE_TAIL, ...FIXED.depart, ...FIXED.arrive, ...FIXED.reroute]);
    const dists = new Set();
    for (let m = 0; m <= 1100; m++) dists.add(speechDist(m));
    dists.forEach(d => LEADS.forEach(l => set.add(l.replace('{d}', d))));
    for (let m = 1500; m <= 1200000; m += 50) set.add('Siga pela trilha por ' + contDist(m) + '.');
    const types = ['turn', 'new name', 'continue', 'merge', 'on ramp', 'off ramp', 'fork', 'end of road', 'roundabout', 'rotary', 'roundabout turn', 'exit roundabout', 'exit rotary', 'notification', 'use lane'];
    const mods = ['', 'uturn', 'sharp right', 'right', 'slight right', 'straight', 'slight left', 'left', 'sharp left'];
    types.forEach(t => mods.forEach(m => [null, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].forEach(exit => {
      const a = action({ type: t, modifier: m, exit }, true);
      set.add(a + '.'); set.add(cap(a) + ' agora.'); set.add(cap(a) + '.');
    })));
    return [...set];
  }

  // ---------- Navegador ----------
  // opts.say({ text, chunks }) é chamado quando há algo a falar.
  class Navigator {
    constructor(route, opts) {
      this.say = (opts && opts.say) || (() => {});
      this.setRoute(route, true);
    }
    setRoute(route, fresh) {
      this.R = route; this.hint = 0; this.spoken = {}; this.off = 0;
      this.arrived = false; this.lastNi = null; this.started = !fresh;
    }
    sp(i) { return this.spoken[i] || (this.spoken[i] = {}); }
    nextIndex(along) {
      const st = this.R.steps;
      for (let i = 1; i < st.length; i++) if (st[i].along > along + 3 && !silent(st[i])) return i;
      return st.length - 1;
    }
    update(f) {
      const rt = this.R, steps = rt.steps;
      const s = snap(rt, [f.lon, f.lat], this.hint);
      const acc = Math.min(f.accuracy || 10, 60);
      if (s.cross > Math.max(35, acc * 1.5)) this.off++; else { this.off = 0; this.hint = s.seg; }
      const offRoute = this.off >= 3 || (this.off >= 2 && s.cross > Math.max(90, acc * 2));
      const along = s.along;
      const ni = this.nextIndex(along);
      const st = steps[ni];
      const dist = Math.max(0, st.along - along);
      const remaining = Math.max(0, rt.total - along);
      const spd = f.speed != null && f.speed >= 0 ? f.speed : 0;
      const F = clamp(spd * 25, 300, 1000), N = clamp(spd * 7, 60, 200);
      let prevAlong = 0;
      for (let i = ni - 1; i > 0; i--) if (!silent(steps[i])) { prevAlong = steps[i].along; break; }
      const gap = st.along - prevAlong;
      const sp = this.sp(ni);
      const u = new Utt();

      if (!offRoute && !this.arrived) {
        if (!this.started) {
          this.started = true;
          addFixed(u, 'depart');
          if (dist > N + 30 && dist <= Math.max(F, 1000)) { addFar(u, st, dist); if (dist <= F) sp.far = true; }
          else if (dist > Math.max(F, 1000)) { addCont(u, dist); sp.cont = true; }
        }
        if (st.type === 'arrive') {
          if (remaining <= 30 || dist <= 30) { this.arrived = true; addFixed(u, 'arrive'); }
          else if (dist <= F && dist > N + 30 && gap > N + 60 && !sp.far) { sp.far = true; addFar(u, st, dist); }
        } else if (dist <= N && !sp.near) {
          sp.near = sp.far = true;
          addNear(u, st);
          const nx = steps.slice(ni + 1).find(x => !silent(x));
          if (nx && nx.type !== 'arrive' && nx.along - st.along < 100) {
            u.add(CHAIN).add(action(nx, true) + '.');
            this.sp(steps.indexOf(nx)).far = true;
          }
        } else if (dist <= F && dist > N + 30 && gap > N + 60 && !sp.far) {
          sp.far = true; addFar(u, st, dist);
        } else if (this.lastNi !== null && ni > this.lastNi && dist > 2000 && !sp.far && !sp.cont) {
          sp.cont = true; addCont(u, dist);
        }
      }
      this.lastNi = ni;
      if (u.chunks.length) this.say(u);

      return {
        snap: s, along, remaining, offRoute, arrived: this.arrived,
        remainingTime: rt.total > 0 ? rt.duration * remaining / rt.total : 0,
        next: st, nextIndex: ni, distToNext: dist
      };
    }
  }

  const api = {
    hav, bearing, buildRoute, snap, pointAt, screenText, screenDist, speechDist, contDist,
    withArticle, action, silent, slug, allChunks, Navigator,
    rerouteUtt: () => addFixed(new Utt(), 'reroute'),
    sampleUtt: () => new Utt().add('Em 300 metros,').add('vire à direita.', 'vire à direita na Avenida Frei Serafim.')
  };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.Nav = api;
})(typeof window !== 'undefined' ? window : globalThis);
