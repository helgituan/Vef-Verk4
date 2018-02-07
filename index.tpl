<!Doctype html>
<html>
<head>
    <title>Verkefni 4</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="/static/styles1.css">
</head>
<body>
    <h1>Verkefni 4</h1>
    <table border="1">
        <tr>
            <th>Kennitala</th>
            <th>Nafn</th>
            <th>Braut</th>
        </tr>
        %for nemandi in bekkur['nemendur']:
            <tr>
                <td><a href="/nemandi/{{nemandi['kt']}}"> {{nemandi['kt']}}</a></td>
                <td>{{nemandi['nafn']}}</td>
                <td>{{nemandi['braut']}}</td>
            </tr>
        %end
    </table>

</body>
</html>