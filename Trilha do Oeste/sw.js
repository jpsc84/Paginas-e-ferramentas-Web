// Service worker da Trilha do Oeste: guarda o app para abrir rápido. Mapa, busca e rotas sempre vêm da rede.
const CACHE = 'trilha-v2';
const CORE = ['./', 'index.html', 'nav.js', 'manifest.json', 'icons/icon.svg', 'icons/icon-192.png', 'icons/icon-512.png', 'icons/apple-touch-icon.png'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith('trilha-') && k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  // Página e motor de navegação: rede primeiro (recebe atualizações), cópia salva sem internet.
  if (req.mode === 'navigate' || (url.origin === self.location.origin && url.pathname.endsWith('/nav.js'))) {
    const key = req.mode === 'navigate' ? 'index.html' : 'nav.js';
    e.respondWith(fetch(req).then(r => { if (r.ok) { const cp = r.clone(); caches.open(CACHE).then(c => c.put(key, cp)); } return r; })
      .catch(() => caches.match(key)));
    return;
  }
  // Biblioteca do mapa e fontes da interface: cópia salva, atualizada em segundo plano.
  if (url.hostname === 'unpkg.com' || url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com') {
    e.respondWith(caches.open(CACHE).then(c => c.match(req).then(hit => {
      const net = fetch(req).then(r => { if (r.ok || r.type === 'opaque') c.put(req, r.clone()); return r; }).catch(() => hit);
      return hit || net;
    })));
    return;
  }
  // Voz gravada: depois de baixado, cada trecho fica salvo.
  if (url.origin === self.location.origin && url.pathname.endsWith('/voz/manifest.json')) {
    e.respondWith(fetch(req).then(r => { if (r.ok) { const cp = r.clone(); caches.open(CACHE).then(c => c.put(req, cp)); } return r; })
      .catch(() => caches.match(req)));
    return;
  }
  if (url.origin === self.location.origin && url.pathname.includes('/voz/')) {
    e.respondWith(caches.open(CACHE).then(c => c.match(req, { ignoreSearch: true }).then(hit => hit || fetch(req).then(r => {
      if (r.ok) c.put(req, r.clone()); return r; }))));
    return;
  }
  // Ícones e demais arquivos do próprio site.
  if (url.origin === self.location.origin) {
    e.respondWith(caches.match(req, { ignoreSearch: true }).then(hit => hit || fetch(req)));
  }
});
