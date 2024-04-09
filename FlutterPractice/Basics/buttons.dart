
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
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: <Widget> [
              ElevatedButton(
                onPressed: null,
                child: const Text('Deactivate'),
              ),
              const SizedBox(height: 30),
              ElevatedButton(
                onPressed: () {print('Pressed');},
                child: const Text('Activate'),
              ),
              const SizedBox(height: 30),
              OutlinedButton(
                onPressed: () {print('pressed outlined button');},
                child: const Text('Outline Button'),
                style: OutlinedButton.styleFrom(
                  backgroundColor: Colors.deepOrange,
                  foregroundColor: Colors.white,
                  shape: const RoundedRectangleBorder(
                    borderRadius: BorderRadius.all(Radius.circular(10))),
                  ),
              ),
            ]
          )
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () {},
          backgroundColor: Colors.red[600],
          child: const Icon(
            Icons.favorite,
            color: Colors.white,
          ),
        )
      ),
      debugShowCheckedModeBanner: false,

    );
  }
}

