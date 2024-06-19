<script>
  export let ex_error; // 부모컴포넌트에서 전달받은 오류
</script>

{#if typeof ex_error.detail === "string"}
  <!-- 문자열 에러 -->
  <!-- <ul>
    <li>{ex_error.detail}</li>
  </ul> -->
  <div class="alert alert-danger" role="alert">
    <div>
      {ex_error.detail}
    </div>
  </div>
{:else if typeof ex_error.detail === "object" && ex_error.detail.length > 0}
  <div class="alert alert-danger" role="alert">
    {#each ex_error.detail as err, i}
      <div>
        <strong>{err.loc[1]}</strong> : {err.msg}
      </div>
    {/each}
  </div>
  <!-- 객체에러 -->
  <!-- <ul>
    {#each ex_error.detail as err, i}
      i는 반복중일때 인덱스값 
      <li>
        <strong>{err.loc[1]}</strong> : {err.msg}
        1은 인덱스값의 두번째 0-body 1-content
      </li>
    {/each}
  </ul> -->
{/if}
