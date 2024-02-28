<script>
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

<h1>{f_message}</h1>

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
