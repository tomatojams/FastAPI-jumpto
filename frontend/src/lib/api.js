// fastapi 함수 url은 호스트명 생략
const fastapi = (
  operation,
  url,
  params,
  success_callback,
  failure_callback
) => {
  // HTTP 메서드와 content type 설정
  let method = operation; // get 또는 post
  let content_type = "application/json";
  //HTTP 요청 헤더 중 "Content-Type" 헤더에 설정되는 값입니다.
  //이 코드에서는 JSON 형식으로 데이터를 서버에 전송할 것이므로, "application/json"으로 설정

  // 매개변수를 JSON 문자열로 변환
  let body = JSON.stringify(params);

  // URL 조립
  let _url = import.meta.env.VITE_SERVER_URL + url;

  // HTTP GET 메서드의 경우 쿼리 매개변수 추가
  if (method === "get") {
    _url += "?" + new URLSearchParams(params);
  }

  // HTTP 요청 옵션 설정
  let options = {
    method: method,
    headers: {
      "Content-Type": content_type, // application/json
    },
  };

  // HTTP GET이 아닌 경우에는 요청 본문(body) 추가
  // GET 요청에서는 별도의 요청 본문이 필요하지 않기 때문
  if (method !== "get") {
    options["body"] = body;
  }

  // fetch 함수로 서버에 요청
  fetch(_url, options).then((response) => {
    if (response.status === 204) {
      // 204 즉 answer을만들때 리턴하지 않는다는 명시
      if (success_callback) {
        success_callback();
      }
      return;
    }
    response
      .json()
      .then((json) => {
        if (response.status >= 200 && response.status < 300) {
          // 200 ~ 299
          // 성공 콜백 호출
          if (success_callback) {
            success_callback(json);
            //API 호출 성공시수행할 함수, 전달된 함수에는 API 호출시 리턴되는 json이 입력으로 주어진다.
            //클라이언트에서 서버로 데이터를 요청하고 성공적인 응답을 받았을 때 UI를 업데이트하거나
            // 특정 동작을 수행하고 싶을 때 success_callback을 활용할 수 있습니다.
          }
        } else {
          // 실패 콜백 호출 또는 경고 표시
          if (failure_callback) {
            failure_callback(json);
            //API 호출 실패시 수행할 함수, 전달된 함수에는 오류 값이 입력으로 주어진다.
          } else {
            alert(JSON.stringify(json));
            // 브라우저에서 간단한 경고 창
          }
        }
      })
      .catch((error) => {
        alert(JSON.stringify(error));
      });
  });
};

// 모듈로 내보내기
export default fastapi;
