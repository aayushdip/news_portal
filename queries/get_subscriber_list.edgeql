
select User {
  name,
  email,
  username,
  admin,
  subscriber,
} filter .subscriber = true
