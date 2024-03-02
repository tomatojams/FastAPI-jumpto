<script>
  import fastapi from "../lib/api";
  // Detail 컴포넌트를 호출할때 전달한 파라미터 값을 읽으려면,params 변수를 선언
  //전달된 파라미터 question_id 값은 params.question_id
  export let params = {};
  let question_id = params.question_id;
  // console.log("question_id:" + question_id);
  let question = {};

  function get_question() {
    fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {
      question = json;
    });
  }
  get_question();
</script>

<h3>{question.subject}</h3>
<div>
  {question.content}
</div>
