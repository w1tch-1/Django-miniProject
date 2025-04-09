$('#orderCreationForm').submit(function (event) {
    event.preventDefault();
    let form = $(this);

    $.ajax(form.attr('action'), {
        type: 'POST',
        data: form.serialize(),
        success: function (response) {
            if (response.success) {
                alert('well done')
            }
        }
    });
});