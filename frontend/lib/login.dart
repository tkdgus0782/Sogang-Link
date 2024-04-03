import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:soganglink/home.dart';
import 'package:http/http.dart' as http;
import 'package:http/testing.dart';
import 'data/login/User.dart';
import 'homepage.dart';
import 'package:fluttertoast/fluttertoast.dart';

class Login extends StatefulWidget {
  const Login({Key? key}) : super(key: key);
  @override
  _Login createState() => _Login();
}

class _Login extends State<Login> {
  final idcontroller = TextEditingController();
  final passwordcontroller = TextEditingController();

  final url = "http://127.0.0.1:8000/login/";

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.only(top: 60.0),
            child: Center(
              child: Container(
                width: 200,
                height: 150,
                /*decoration: BoxDecoration(
                        color: Colors.red,
                        borderRadius: BorderRadius.circular(50.0)),*/
                child: Icon(Icons.logo_dev),
              ),
            ),
          ),
          Padding(
            //padding: const EdgeInsets.only(left:15.0,right: 15.0,top:0,bottom: 0),
            padding: EdgeInsets.symmetric(horizontal: 15),
            child: TextField(
              controller: idcontroller,
              decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'id',
                  hintText: 'Enter id'),
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(
                left: 15.0, right: 15.0, top: 15, bottom: 0),
            //padding: EdgeInsets.symmetric(horizontal: 15),
            child: TextField(
              obscureText: true,
              controller: passwordcontroller,
              decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Password',
                  hintText: 'Enter secure password'),
            ),
          ),
          SizedBox(
            height: 200,
          ),
          Container(
            height: 50,
            width: 250,
            decoration: BoxDecoration(
                color: Colors.blue, borderRadius: BorderRadius.circular(20)),
            child: TextButton(
              onPressed: () async {
                try {
                  var request = Uri.parse(url);
                  print(idcontroller.text); // 개발 과정에서만 사용하세요. 실제 앱에서는 제거해야 합니다.
                  print(passwordcontroller
                      .text); // 개발 과정에서만 사용하세요. 실제 앱에서는 제거해야 합니다.

                  final response = await http.post(request, body: {
                    "username": idcontroller.text,
                    "password": passwordcontroller.text
                  });

                  if (response.statusCode == 200) {
                    Navigator.pushAndRemoveUntil(
                        context,
                        MaterialPageRoute(
                            builder: (BuildContext context) => Home()),
                        (route) => false);
                  } else {
                    Fluttertoast.showToast(
                        msg: "로그인 실패",
                        toastLength: Toast.LENGTH_SHORT,
                        gravity: ToastGravity.CENTER,
                        timeInSecForIosWeb: 1,
                        backgroundColor: Colors.red,
                        textColor: Colors.white,
                        fontSize: 16.0);
                  }
                } catch (e) {
                  Fluttertoast.showToast(
                      msg: "네트워크 오류",
                      toastLength: Toast.LENGTH_SHORT,
                      gravity: ToastGravity.CENTER,
                      timeInSecForIosWeb: 1,
                      backgroundColor: Colors.red,
                      textColor: Colors.white,
                      fontSize: 16.0);
                }
              },
              child: Text(
                'Login',
                style: TextStyle(color: Colors.white, fontSize: 25),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
