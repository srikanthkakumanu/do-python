<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="/public/styles.css">
    <title>Bottle</title>
</head>
<body>
    <header>
        <h1>Ninja Town</h1>
    </header>
    <main>
        Welcome Ninja Town
        <ul>
    % for ninja in ninjas:
    <li>
      <div>{{ninja['name']}} - {{ninja['belt_color']}} belt</div>
      <div>Special move - {{ninja['speciality']}}</div>
    </li>
    % end
  </ul>
    </main>
    <footer>
        <p>Ninja Town API</p>
    </footer>
</body>
</html>