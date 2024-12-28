<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Calendrier</h1>
    <div v-for="event in events" :key="event.id" class="border p-4 rounded mb-2">
      <h2 class="font-semibold">{{ event.summary }}</h2>
      <p class="text-gray-600">Date : {{ event.date }}</p>
      <p class="text-gray-600">Description : {{ event.description }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      events: [],
    };
  },
  async mounted() {
    const response = await axios.get("/api/calendar/");
    this.events = response.data.events;
  },
};
</script>
