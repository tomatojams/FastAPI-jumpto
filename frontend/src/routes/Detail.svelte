<script>
  import fastapi from "../lib/api";
  // Detail 컴포넌트를 호출할때 전달한 파라미터 값을 읽으려면,params 변수를 선언
  //전달된 파라미터 question_id 값은 params.question_id
  export let params = {};
  let question_id = params.question_id;
  let question = { answer_list: [] };
  // question 변수의 초깃값을 {}에서 {answer_list:[]}으로 변경, each문에서 answer_list를 참고있기때문에
  let content = "";

  function get_question() {
    fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {
      question = json;
    });
  }
  get_question();

  function post_answer(event) {
    event.preventDefault();
    let url = "/api/answer/create/" + question_id;
    let params = {
      content: content,
    };
    fastapi("post", url, params, (json) => {
      content = ""; // 등록에 성공하면 textarea를 지움
      get_question(); // 상세화면에 새로운 결과값을 반영
    });
  }
</script>

<h3>{question.subject}</h3>
<div>
  {question.content}
</div>
<ul>
  {#each question.answer_list as answer_list}
    <li>{answer_list.content}</li>
  {/each}
</ul>
<form method="post">
  <textarea rows="15" bind:value={content}></textarea>
  <input type="submit" value="답변등록" on:click={post_answer} />
</form>
