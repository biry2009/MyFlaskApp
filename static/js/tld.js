/**
 * Created by Bing on 2018/2/5.
 */

$(document).ready(function () {
    $('#example').DataTable({
        "dom": 'tp'
    });

    var table = $('#example').DataTable();

    $('#search-domain').keyup(function () {
        table.search($(this).val()).draw();
    })
});