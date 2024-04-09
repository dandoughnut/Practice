
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Practice'),
        backgroundColor: Colors.red[200],),
        body: Container(
          child: Column(
            children: <Widget> [
              TextField(
                keyboardType: TextInputType.emailAddress,
                controller: TextEditingController(),
                decoration: InputDecoration(
                  labelText: 'Email',
                  hintText: 'you@email.com',
                  icon: Icon(Icons.mail_outline),
                ),
              ),

              TextField(
                keyboardType: TextInputType.number,
                controller: TextEditingController(),
                decoration: InputDecoration(
                  labelText: 'SSN',
                  hintText: '940710-1000000',
                  icon: Icon(Icons.calculate_outlined),
                ),
                maxLength: 14,
                inputFormatters: [FilteringTextInputFormatter.allow(RegExp('[0-9]'))],
              ),
              TextField(
                  controller: TextEditingController(),
                  keyboardType: TextInputType.visiblePassword,
                  obscureText: true,
                  decoration: InputDecoration(
                    labelText: 'Password',
                    icon: Icon(Icons.password),
                  ),
                  maxLength: 25,
                )

            ]
          )
        )
      ),
      debugShowCheckedModeBanner: false,

    );
  }
}

