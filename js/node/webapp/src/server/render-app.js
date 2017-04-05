// @flow

import { APP_CONTAINER_CLASS, STATIC_PATH, WDS_VIRTUAL_PATH } from '../shared/config';
import { isProd } from '../shared/util';

const renderApp = (title: string) =>
`<!doctype html>
<html>
  <head>
    <title>${title}</title>
    <link rel="stylesheet" href="${STATIC_PATH}/css/style.css">
  </head>
  <body>
    <div class="${APP_CONTAINER_CLASS}"></div>
    <script src="${isProd ? STATIC_PATH : WDS_VIRTUAL_PATH}/js/bundle.js"></script>
  </body>
</html>
`;

export default renderApp
