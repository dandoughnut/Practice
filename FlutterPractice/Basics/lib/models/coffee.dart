class Coffee {
  final String id;
  final String title;
  final String price;
  final String imageUrl;
  final String imageUrl2;

  Coffee ({
    required this.id,
    required this.title,
    required this.price,
    required this.imageUrl,
    required this.imageUrl2,
  });
}

List<Coffee> coffees = [
  Coffee (
    id: '01',
    title: "Americano",
    price: "4500",
    imageUrl: "lib/assets/images/coffee01.jpeg",
    imageUrl2: "lib/assets/images/coffee01_ice.jpeg",
  ),
  Coffee (
    id: '02',
    title: "Latte",
    price: "5000",
    imageUrl: "lib/assets/images/coffee02.jpeg",
    imageUrl2: "lib/assets/images/coffee02_ice.jpeg",
  ),
  Coffee (
    id: '03',
    title: "Macchiato",
    price: "5500",
    imageUrl: "lib/assets/images/coffee03.jpeg",
    imageUrl2: "lib/assets/images/coffee03_ice.jpeg",
  ),
];