CREATE TABLE `airline` (
  `id` int,
  `Airline_name` text,
  `Airline_code` text,
  `Number_of_planes` int,
  PRIMARY KEY (`id`, `Airline_code`)
);

CREATE TABLE `Airport` (
  `id` int PRIMARY KEY,
  `Airline_code` text,
  `Airport_name` text,
  `city` text,
  `country` text
);

CREATE TABLE `Route` (
  `Destinations` int,
  `route_id` int[pk]
);

CREATE TABLE `Aeroplane` (
  `airport_id` int PRIMARY KEY,
  `number_of_flights` int,
  `capacity` int,
  `Airline_code` text,
  `route_id_id` int
);

ALTER TABLE `Airport` ADD FOREIGN KEY (`Airline_code`) REFERENCES `airline` (`Airline_code`);

ALTER TABLE `Aeroplane` ADD FOREIGN KEY (`route_id_id`) REFERENCES `Route` (`route_id`);
