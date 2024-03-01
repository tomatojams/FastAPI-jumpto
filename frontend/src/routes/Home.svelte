<script>
  import fastapi from "../lib/api";  // fastapi 함수
  import {link} from 'svelte-spa-router'

  let question_list = [];

  function get_question_list() {
    fastapi("get", "/api/question/list", {}, (json) => {
      question_list = json;
    });
    //  url은/ 부터 시작,패러미터없음, success_callback 응답받은 json을 리스트에 넣어라 failure_callback은 생략
  }

  get_question_list();

  //   function get_question_list() {
  //     fetch("http://127.0.0.1:8000/api/question/list").then((response) => {
  //       response.json().then((json) => {
  //         question_list = json;
  //       });
  //     });
  //   }
</script>

<ul>
  {#each question_list as question}
    <li><a use:link href="/detail/{question.id}">{question.subject}</a></li>
  {/each}
</ul>
<!-- SPA Router를 사용하여 페이지를 변경 -->
<!-- a 태그에 use:link 속성을 사용하기 위해 link를 import를 했다.
use:link 속성을 사용한 경우는 항상 /# 문자가 선행되도록 경로가 만들어진다. 
웹 페이지에서 어떤 경로가 /#으로 시작하면 브라우저는 이 경로를 하나의 페이지로 인식한다. 
즉, 브라우저는 http://127.0.0.1:5173/#/some-path, http://127.0.0.1:5173/#/question-create 
두 개의 경로를 모두 동일한 페이지로 인식한다는 점이다. 
이러한 것을 해시 기반 라우팅(hash based routing)이라고 한다.
브라우저는 /# 으로 시작하는 URL은 동일한 페이지라고 인식하기 때문에 
서버로 페이지 요청을 보내지 않기 때문이다.-->
