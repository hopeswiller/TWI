$("#alert").alert().fadeTo(2000, 500).slideUp(500, function () {
    $("#alert").slideUp(500);
});

const options = {
    defaultDate: new Date(),
    format: 'L'
}
$(function () {
    $('#datetimepicker').datetimepicker(options);
    $('#startdatepicker').datetimepicker(options);
    $('#enddatepicker').datetimepicker({
        format: 'L'
    });
});
