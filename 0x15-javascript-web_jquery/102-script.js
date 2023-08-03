$(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function(resp) {
      $('#hello').text(resp.hello);
    })
  });
});
