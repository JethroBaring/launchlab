<!-- Cj -->
<!-- gamita sa ang startup.png sa static paras picture -->
<script>
    let email = "";
  let password = "";

  const handleLogin = () => {
    // Add your login logic here
    console.log("Email:", email);
    console.log("Password:", password);
  };
</script>
<style>

</style>

<head>
    <meta charset="utf-8" />
    <link rel="icon" href="./logo.png" />
    <meta name="viewport" content="width=device-width", initial-scale=1 />

    <link href="./_app/immutable/assets/0.17d7b5b5.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
</head>

<body>
    <div style="width: 100%; height: 100%; padding-top: 121px; padding-bottom: 120px; padding-left: 219px; background: #F8FAFC; justify-content: flex-end; align-items: center; display: inline-flex">
        <div style="width: 2378.57px; height: 722px; position: relative">
          <div style="width: 1482px; height: 722px; left: 0px; top: 0px; position: absolute; background: white; box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.25); border-radius: 25px; border: 0.30px #E6E6E6 solid"></div>
          <div style="width: 1637.57px; height: 417.55px; left: 741px; top: 144.78px; position: absolute">
            <div style="width: 320.62px; height: 57.15px; left: 31.80px; top: 0px; position: absolute; color: #394E6A; font-size: 32px; font-family: Inter; font-weight: 600; word-wrap: break-word">Login</div>
      
            <!-- Email Input -->
            <div style="width: 320.62px; height: 57.15px; left: 31.80px; top: 75px; position: absolute; color: #394E6A; font-size: 15px; font-family: Inter; font-weight: 600; word-wrap: break-word">Email</div>
            <div style="width: 500px; height: 57.15px; left: 30px; top: 100px; position: absolute; color: #394E6A; font-size: 20px; font-family: Inter; font-weight: 400; word-wrap: break-word">
              <!-- <label for="email">Email</label> -->
              <input bind:value={email} type="text" id="email" placeholder="email" style="width: 100%; height: 100%; padding: 15px; border: 1px solid #8793A1; border-radius: 10px;">
            </div>
      
            <!-- Password Input -->
            <div style="width: 320.62px; height: 57.15px; left: 31.80px; top: 170px; position: absolute; color: #394E6A; font-size: 15px; font-family: Inter; font-weight: 600; word-wrap: break-word">Password</div>
            <div style="width: 500px; height: 57.15px; left: 30px; top: 200px; position: absolute; color: #394E6A; font-size: 20px; font-family: Inter; font-weight: 400; word-wrap: break-word">
              <!-- <label for="password">Password</label> -->
              <input bind:value={password} type="password" id="password" placeholder="password" style="width: 100%; height: 100%; padding: 15px; border: 1px solid #8793A1; border-radius: 10px;">
            </div>
      
            <!-- Login Button -->
            <div style="width: 211.98px; height: 45.72px; left: 30px; top: 300px; position: absolute">
              <button on:click={handleLogin} style="width: 80%; height: 130%; border: none; background: #1C83E5; color: white; font-size: 16px; font-family: Inter; font-weight: 500; cursor: pointer; border-radius: 10px; box-shadow: 1px 4px 4px rgba(24.94, 99.88, 220, 0.50);">Login</button>
            </div>
          </div>
      
          <!-- Logo and Project Name -->
          <div style="width: 231px; height: 37.23px; left: 23px; top: 18.10px; position: absolute">
            <img style="width: 40px; height: 37.23px; left: 0px; top: 0px; position: absolute" src="static/launchlab_logo.png"/>
            <div style="width: 179px; height: 36.20px; left: 52px; top: 0.95px; position: absolute; color: #042B59; font-size: 30px; font-family: Inter; font-weight: 700; word-wrap: break-word">LaunchLab</div>
          </div>
        </div>
      </div>
</body>