<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Contacts</h1>
    <div v-for="contact in contacts" :key="contact.email" class="border p-4 rounded mb-2">
      <h2 class="font-semibold">{{ contact.name }}</h2>
      <p class="text-gray-600">Email : {{ contact.email }}</p>
      <p class="text-gray-600">Téléphone : {{ contact.phone }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      contacts: [],
    };
  },
  async mounted() {
    const response = await axios.get("/api/contacts/");
    this.contacts = response.data.contacts;
  },
};
</script>
