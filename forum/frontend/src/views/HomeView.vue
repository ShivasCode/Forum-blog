<template>
  <div class="home mt-3">
    <div class="container">
      <div v-for="discussion in discussions" :key="discussion.uuid">
        <div class="shadow p-3 mb-5 bg-body rounded">
          <div class="card-body">
            <p class="mb-0">
              Posted by:
              <span class="discussion-author">{{ discussion.user }}</span>
            </p>
            <router-link
              class="discussion-link"
              :to="{ name: 'discussion', params: { slug: discussion.slug } }"
              ><h2>{{ discussion.title }}</h2></router-link
            >
            <p class="mb-0">Answers: {{ discussion.answers_count }}</p>
          </div>
        </div>
      </div>
      <div class="my-4">
        <p v-show="loading">...loading...</p>
        <button
          v-show="next"
          @click="getDiscussions"
          class="btn btn-sm btn-outline-success"
        >
          Load More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { axios } from "@/common/api.service.js";

export default {
  name: "HomeView",
  data() {
    return {
      discussions: [],
      next: null,
      loading: false,
    };
  },
  components: {},
  methods: {
    async getDiscussions() {
      let endpoint = "/api/v1/discussions/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loading = true;
      try {
        const response = await axios.get(endpoint);
        this.discussions.push(...response.data.results);
        if (response.data.next) {
          this.next = response.data.next;
        } else {
          this.next = null;
        }
        this.loading = false;
        console.log(response);
      } catch (error) {
        console.log(error.response);
      }
    },
  },
  created() {
    this.getDiscussions();
  },
};
</script>

<style>
.discussion-author {
  font-weight: bold;
  color: #dc3545;
}

.discussion-link {
  font-weight: 400;
  color: black;
  text-decoration: none;
}

.discussion-link:hover {
  color: #343a40;
}
</style>
