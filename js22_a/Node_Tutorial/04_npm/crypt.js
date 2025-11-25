// TODO: カスタム暗号化モジュールのインポート: ./utils/cryptoUtil.js
// メソッド: encrypt, decrypt, generateKey
//reqで入力
const { decrypt } = require('dotenv');
const { encrypted, decrypted, generateKey, encrypt } = require('./utils/cryptoUtil');
// 鍵の生成
const message = "Hello";
const key = generateKey("mySecretKey");
// TODO: メッセージを暗号化
const encrypted = encrypt(message, key);
// TODO: 暗号文を復号化
const decrypted = decrypt(encrypted, key);

// 結果表示
let result = { message, encrypted, decrypted };
console.table(result);