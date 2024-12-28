import Vue from "vue";
import Router from "vue-router";
import Dashboard from "./components/Dashboard.vue";
import Emails from "./components/Emails.vue";
import Contacts from "./components/Contacts.vue";
import Calendar from "./components/Calendar.vue";

Vue.use(Router);

export default new Router({
  routes: [
    { path: "/", component: Dashboard },
    { path: "/emails", component: Emails },
    { path: "/contacts", component: Contacts },
    { path: "/calendar", component: Calendar },
  ],
});
