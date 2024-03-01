<script>
// Detail 컴포넌트를 호출할때 전달한 파라미터 값을 읽으려면,params 변수를 선언
//전달된 파라미터 question_id 값은 params.question_id
  export let params = {};
  
  let question_id = params.question_id;
  console.log("question_id:" + question_id);
</script>

<h1>제목</h1>
<div>내용</div>
