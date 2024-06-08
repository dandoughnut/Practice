import 'package:flutter/material.dart';
import 'package:cafe_app/models/coffee.dart';

class MenuDetailScreen extends StatefulWidget {
  const MenuDetailScreen({super.key, required this.item});
  final Coffee item;

  @override
  _MenuDetailScreenState createState() => _MenuDetailScreenState();
}

class _MenuDetailScreenState extends State<MenuDetailScreen> {
  @override
  String? choice = 'hot';

  Widget build (BuildContext context) {
    Coffee thisCoffee = widget.item;
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Coffee & Beverages',
          style: TextStyle(color: Colors.black),
        ),
        centerTitle: true,
        backgroundColor: Colors.white,
        leading: const BackButton(
          color: Colors.grey,
        ),
     ),
      body: ListView(
        children: [
          Padding(
            padding: const EdgeInsets.all(40.0),
            child: Column(
              children: [
                ClipRRect(
                  borderRadius: BorderRadius.circular(16.0),
                  child: Image.asset(
                      choice == 'hot' ? "${thisCoffee.imageUrl}" : "${thisCoffee.imageUrl2}"),
                ),
                Text(
                  "${thisCoffee.title}",
                  style: Theme.of(context).textTheme.titleLarge,
                ),
                Text(
                  "${thisCoffee.price} KRW",
                  style: Theme.of(context).textTheme.bodyMedium,
                )
              ]
            )
          ),
          Divider(),
          Padding(
            padding: const EdgeInsets.only(left: 20.0),
            child: Text(
              "Hot/Iced", style: Theme.of(context).textTheme.titleMedium,
            )
          ),
          Row(
            children: [
              ChoiceChip(
                padding: EdgeInsets.all(8.0),
                label: SizedBox(
                  width: 140,
                  child: Text('Hot', textAlign: TextAlign.center),
                ),
                selected: choice == 'hot',
                onSelected: (selected) {
                  setState(() {
                    choice = 'hot';
                  });
                },
                selectedColor: Colors.white,
                  shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(5.0),
                  side: BorderSide(
                    color: choice == 'hot' ? Colors.black : Colors.grey),
                  ),

              ),

              ChoiceChip(
                padding: EdgeInsets.all(8.0),
                label: SizedBox(
                  width: 140,
                  child: Text('Iced', textAlign: TextAlign.center),
                ),
                selected: choice == 'ice',
                onSelected: (selected) {
                  setState(() {
                    choice = 'ice';
                  });
                },
                selectedColor: Colors.white,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(5.0),
                  side: BorderSide(
                    color: choice == 'ice' ? Colors.black : Colors.grey),
                  ),
                ),


            ]
          )

        ]
      ),
      bottomNavigationBar: BottomAppBar(
        color: Colors.black87,
        child: Row(
          children: [
            Container(
              width: 100,
              height: 60,
              color: Colors.red,
            ),
            Expanded(
              child: Padding(
                padding: EdgeInsets.all(8.0),
                child: Text(
                  "${thisCoffee.price} KRW",
                  style: TextStyle(color: Colors.white, fontSize: 18),
                )
              )
            ),
            TextButton(
              child: Text(
                "Order",
                style: TextStyle(color: Colors.red, fontSize: 22),
              ),
              onPressed: () {
                showDialog(
                  context: context,
                  builder: (BuildContext context) {
                    return AlertDialog(
                      title: Text('${thisCoffee.title}'),
                      content: Text('${thisCoffee.price}'),
                      actions: <Widget>[
                        TextButton(
                          onPressed: () => Navigator.pop(context, 'Cancel'),
                          child: const Text('Cancel'),

                        ),
                        TextButton(
                          onPressed: () => Navigator.pop(context, 'OK'),
                          child: const Text('Confirm'),
                        )
                      ]
                    );
                  }
                );
              },
            )

          ]
        )
    )
    );

  }
}