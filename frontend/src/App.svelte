<script>
  // 컴포넌트 불러옴
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"

  const routes = {
    '/': Home, //Home.svelte 파일의 내용 컴포넌트, 라우팅 경로와 해당경로에 매핑되는 Svelte 컴포넌트를 정의
    '/detail/:question_id': Detail, 
    //  Detail 컴포넌트에 전달, 뒤의 숫자는 Detail 컴포넌트에 question_id로 전달이 된다.
  }
</script>

<Router {routes}/> 
<!-- 동적으로 페이지변경위해 html에 있음
Router 컴포넌트를 사용하여 라우팅을 설정, SPA Router로 동적전환
전체페이지를 다시 로드안해도 주소에 따른 컴포넌트만 로드
 -->




















<!-- <script>
  let question_list = [];

  function get_question_list() {
    fetch("http://127.0.0.1:8000/api/question/list").then((response) => {
      response.json().then((json) => {
        question_list = json;
      });
    });
  }

  get_question_list();
</script>

<ul>
  {#each question_list as question}
    <li>{question.id} : {question.subject}: "{question.content}"</li>
  {/each}
</ul> -->

<!-- <script>
  let f_message; // 변수 f_message를 정의

  // GET 메서드를 사용하여 "http://127.0.0.1:8000/hello" 주소로 요청을 보냄
  fetch("http://127.0.0.1:8000/hello").then((response) => {
    // 응답을 받은 후에 실행될 함수를 정의
    response.json().then((json) => {
      // 받은 응답을 JSON으로 파싱하고 그 결과를 변수 f_message에 저장
      f_message = json.message;
    });
  });
</script>

<h1>{f_message}</h1> -->

<!-- 비동기식 -->
<!-- <script>
  async function hello() {
    const res = await fetch("http://127.0.0.1:8000/hello");
    const json = await res.json();

    if (res.ok) {
      return json.message;
    } else {
      alert("error");
    }
  }

  let promise = hello();
</script>

{#await promise}
  <p>...waiting</p>
{:then message}
  <h1>{message}</h1>
{/await} -->
