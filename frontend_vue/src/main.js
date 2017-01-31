// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import VueRouter from 'vue-router';
import VueResource from 'vue-resource'; // --> https://github.com/mzabriskie/axios
import App from './App';

import Home from './components/Home';
import Error403 from './components/Error403';
import Error404 from './components/Error404';
import Login from './components/Login';
import Search from './components/Search';
import Artists from './components/Artists';
import Artworks from './components/Artworks';
import Events from './components/Events';
import Venues from './components/Venues';

Vue.use(VueRouter);
Vue.use(VueResource);

const routes = [
  { path: '/', component: Home },
  { path: '/403', component: Error403 },
  { path: '/404', component: Error404 },
  { path: '/login', component: Login },
  { path: '/search', component: Search },
  { path: '/artists', component: Artists },
  { path: '/artworks', component: Artworks },
  { path: '/events', component: Events },
  { path: '/venues', component: Venues },
];

const router = new VueRouter({
  routes, // short for routes: routes
  mode: 'history',
});

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  template: '<App/>',
  components: { App },
});
