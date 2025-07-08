const { app, BrowserWindow } = require('electron');
const path = require('path');
const { exec } = require('child_process');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    },

    icon: path.join(__dirname, 'assets/logo.ico') // Sesuaikan path sesuai lokasi logo
  });

  // Akses aplikasi Flask yang berjalan di localhost
  mainWindow.loadURL('http://127.0.0.1:5000');
  
  mainWindow.on('closed', function () {
    mainWindow = null;
  });
}

app.on('ready', function () {
  // Jalankan aplikasi Flask menggunakan subprocess Python
  const flaskProcess = exec('python harga.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing Flask app: ${error}`);
      return;
    }
    console.log(stdout);
  });

  createWindow();
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow();
  }
});
