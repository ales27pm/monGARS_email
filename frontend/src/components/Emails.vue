<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Courriels</h1>
    <div v-for="(category, index) in ['urgent', 'medium', 'low']" :key="index" class="mb-6">
      <h2 class="text-xl font-semibold capitalize mb-2">{{ category }}</h2>
      <div v-for="email in emails[category]" :key="email.id" class="border p-4 rounded mb-2">
        <h3 class="font-semibold">{{ email.subject }}</h3>
        <p class="text-gray-600">De : {{ email.sender }}</p>
        <p class="mt-2">{{ email.analysis }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      emails: { urgent: [], medium: [], low: [] },
    };
  },
  async mounted() {
    const response = await axios.post("/api/emails/process", { user_input: "Analyze my emails" });
    this.emails = response.data.processed_emails;
  },
};
</script>
