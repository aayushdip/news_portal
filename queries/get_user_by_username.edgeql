# getUserByUsername.edgeql

select User {
  name,
  email,
  username,
  admin,
  subscriber,
} filter .username = <str>$0
