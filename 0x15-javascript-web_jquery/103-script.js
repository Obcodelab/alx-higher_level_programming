$(function() {
  function fetchTranslation() {
    const languageCode = $('#language_code').val();

    $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function(resp) {
      $('#hello').text(resp.hello);
    })
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function(event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });
});
