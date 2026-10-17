export async function onRequest(context) {
  const url = new URL(context.request.url);
  if (
    url.hostname === 'game.baeksefood.com' &&
    (url.pathname === '/' || url.pathname === '/index.html')
  ) {
    url.pathname = '/game/';
    return context.env.ASSETS.fetch(url);
  }
  return context.next();
}
