$(document).ready(() => {
    const languageCode = $('input#language_code').val()

    $(document).on('keydown', (e) => {
        if (e.key === 'Enter') {
            ajaxCall()
            console.log(languageCode);

        }
    })

    $('input#btn_translate').on('keydown', ajaxCall)

    const ajaxCall =
        $.ajax({
            type: "get",
            url: `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`,
            dataType: "json",
            success: function (response) {
                console.log(response.hello);
            }
        });
    }
})