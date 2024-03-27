
import 'package:flutter/material.dart';

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
        body: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            Container(
              margin: const EdgeInsets.all(10.0),
              width: 80,
              height: 80,
              color: Colors.cyan[600],
            ),
            Container(
              margin: const EdgeInsets.all(10.0),
              width: 90,
              height: 90,
              color: Colors.amber[600],
            ),
            Container(
              margin: const EdgeInsets.all(10.0),
              width: 100,
              height: 100,
              color: Colors.red[600],
              child: Column(
                children: <Widget> [
                  Image.network('https://picsum.photos/200?image=30', width: 100, height: 100, fit: BoxFit.cover,),
                  const SizedBox(height: 20.0,),
                  Image.network('https://picsum.photos/200?image=30', width: 100, height: 100, fit: BoxFit.cover,),
                ]
              )
            )
          ]
        )
      ),
      debugShowCheckedModeBanner: false,

    );
  }
}

