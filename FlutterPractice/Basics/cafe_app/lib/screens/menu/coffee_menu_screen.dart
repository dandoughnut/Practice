import 'package:flutter/material.dart';
import 'package:cafe_app/models/coffee.dart';
import 'package:cafe_app/screens/menu/menu_detail_screen.dart';

class CoffeeMenuScreen extends StatelessWidget {
  const CoffeeMenuScreen({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return ListView(
      children: List.generate(
        coffees.length,
          (index) => Container(
            height: 150.0,
            child: GestureDetector(
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute( builder: (context) => MenuDetailScreen(item: coffees[index]),)
                );
              },
              child: Padding(
                  padding: EdgeInsets.all(16.0),
                  child: Row(
                      children: [
                        Image.asset("${coffees[index].imageUrl}", height: 150, width: 150, fit: BoxFit.fill),
                        Padding(
                            padding: EdgeInsets.all(8.0),
                            child: Column (
                                mainAxisAlignment: MainAxisAlignment.center,
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text("${coffees[index].title}",
                                    style: Theme.of(context).textTheme.titleLarge,),
                                  Text("${coffees[index].price} KRW",
                                    style: Theme.of(context).textTheme.titleMedium,),
                                ]
                            )
                        )
                      ] //
                  )
              )
            )

          ),
      ),
    );
  }
}