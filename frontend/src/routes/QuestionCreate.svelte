<script>
  import { push } from "svelte-spa-router";
  import fastapi from "../lib/api";
  import Error from "../components/Error.svelte";

  let error = { details: [] };
  let subject = "";
  let content = "";

  function post_question(event) {
    event.preventDefault();
    let url = "/api/question/create";
  }
</script>
