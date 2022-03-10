<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Login MIA</title>
    </head>

    <body class="outer">
        <div class="inner">
            <div>
                <?php
                    if (isset($_POST['username']) && isset($_POST['password'])) {
                        if ($_POST['username'] === 'admin' && hash('tiger160,4', $_POST['password'], false) == '0') {
                            include('flag.php');
                            echo "<h2>$flag</h2>";
                        }
                    } else {
                        echo '<h2>Find the magical hash collision!</h2>';
                    }

                    $source = show_source("index.php", true);
                    print $source;
                ?>
            </div>
        </div>
    </body>
</html>
