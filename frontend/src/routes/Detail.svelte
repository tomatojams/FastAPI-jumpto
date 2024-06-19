<script>
  import fastapi from "../lib/api";
  // Detail 컴포넌트를 호출할때 전달한 파라미터 값을 읽으려면,params 변수를 선언
  //전달된 파라미터 question_id 값은 params.question_id
  import Error from "../components/Error.svelte";
  export let params = {};
  let question_id = params.question_id;
  let question = { answer_list: [] };
  // question 변수의 초깃값을 {}에서 {answer_list:[]}으로 변경, each문에서 answer_list를 참고하고 있기때문에
  let content = "";
  let err = { detail: [] };

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
    fastapi(
      "post",
      url,
      params,
      (json) => {
        content = ""; // 등록에 성공하면 textarea를 지움
        err = { detail: [] }; // 에러메시지를 초기화
        get_question(); // 상세화면에 새로운 결과값을 반영
      },
      (err_json) => {
        err = err_json;
      }
    );
  }
</script>

<div class="container my-3">
  <h2 class="border-bottom py-2">{question.subject}</h2>
  <div class="card my-3">
    <div class="card-body">
      <div class="card-text" style="white-space: pre-line;">
        {question.content}
      </div>
      <div class="d-flex justify-content-end">
        <div class="badge bg-light text-dark p-2">
          {question.create_date}
        </div>
      </div>
    </div>
  </div>

  <h5 class="border-bottom my-3 py-2">
    {question.answer_list.length}개의 답변이 있습니다.
  </h5>
  {#each question.answer_list as answer}
    <div class="card my-3">
      <div class="card-body">
        <div class="card-text" style="white-space: pre-line;">
          {answer.content}
        </div>
        <div class="d-flex justify-content-end">
          <div class="badge bg-light text-dark p-2">
            {answer.create_date}
          </div>
        </div>
      </div>
    </div>
  {/each}

  <Error ex_error={err} />
  <form method="post" class="my-3">
    <div class="mb-3">
      <textarea rows="10" bind:value={content} class="form-control" />
    </div>
    <input
      type="submit"
      value="답변등록"
      class="btn btn-primary"
      on:click={post_answer}
    />
  </form>
</div>

<!-- <h3>{question.subject}</h3>
<div>
  {question.content}
</div>
<ul>
  {#each question.answer_list as answer_list}
    <li>{answer_list.content}</li>
  {/each}
</ul>
<Error ex_error={err} />
에러 컴포넌트
<form method="post">
  <textarea rows="15" bind:value={content}></textarea>
  <input type="submit" value="답변등록" on:click={post_answer} />
</form> -->
