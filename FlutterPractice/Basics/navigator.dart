import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  static const String _title = 'Flutter Code Sample';
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: _title,
      home: MyStatefulWidget(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class MyStatefulWidget extends StatefulWidget {
  const MyStatefulWidget({Key? key}) : super(key: key);

  @override
  State<MyStatefulWidget> createState() => _MyStatefulWidgetState();
}

class _MyStatefulWidgetState extends State<MyStatefulWidget> {
  int _selectedIndex = 0;
  @override
  static const List<Widget> _widgetOptions = <Widget>[
    Text('0th: Home', style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold)),
    Text('1st: Search', style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold)),
    Text('2nd: Profile', style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold)),
  ];
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('BottomNavigationBar Sample'),
      ),
      body: Center(
        child: _widgetOptions.elementAt(_selectedIndex),
      ),
      bottomNavigationBar: BottomNavigationBar (
        type: BottomNavigationBarType.shifting,
        selectedItemColor: Colors.yellowAccent,
        unselectedItemColor: Colors.grey[50],
        currentIndex: _selectedIndex,
        items: const <BottomNavigationBarItem> [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home', backgroundColor: Colors.indigo),
          BottomNavigationBarItem(icon: Icon(Icons.search), label: 'Search', backgroundColor: Colors.deepOrange),
          BottomNavigationBarItem(icon: Icon(Icons.person_outline), label: 'Profile', backgroundColor: Colors.deepPurple),
        ],
        onTap: (int index) {
          setState(() {
            _selectedIndex = index;
          });
        },
      )


    );
  }
}