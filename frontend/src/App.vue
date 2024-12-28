<template>
    <div id="app">
      <nav class="bg-gray-800 p-4 text-white flex space-x-4">
        <router-link to="/" class="hover:underline">Dashboard</router-link>
        <router-link to="/emails" class="hover:underline">Emails</router-link>
        <router-link to="/contacts" class="hover:underline">Contacts</router-link>
        <router-link to="/calendar" class="hover:underline">Calendar</router-link>
      </nav>
      <router-view />
    </div>
  </template>
  
  <script>
  export default {
    name: "App",
  };
  </script>
  
  <style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9fafb;
  }
  </style>