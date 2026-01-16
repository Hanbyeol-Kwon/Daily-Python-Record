show dbs
use test2 //만들고 싶은 데이터베이스 이름 넣고 그냥 use 쓰면 됨. 근데 옆에 보여지지는 않음. (table-collection)이 안 만들어졌기 때문.
db.createCollection("class")

use test
db.createCollection("class") //collection(=table) 위주로 돌아가기 때문에 표가 없으면 db가 보이지 않음. 약간의 객체지향 언어
db.createCollection("log", {capped: true, size: 5242880, max: 5000}) // 가변길이, 행 수는 5000까지
db.class.renameCollection("product")
show collections
db.log.find()
db.stats()
db.dropDatabase()
use test2
db.class.drop()
use test2
db.dropDatabase()


use dodream
db.createCollection("class")
db.class.insertOne(
    {subject: "mongdb", author:"nevaeh", views:10000000}
)
db.class.find()

db.class.insertMany(
    [
        { subject: "coffee", author: "xyz", views: 50 },
         { subject: "Coffee Shopping", author: "efg", views: 5 },
         { subject: "Baking a cake", author: "abc", views: 90  },
         { subject: "baking", author: "xyz", views: 100 },
         { subject: "Café Con Leche", author: "abc", views: 200 },
         { subject: "Сырники", author: "jkl", views: 80 },
         { subject: "coffee and cream", author: "efg", views: 10 },
         { subject: "Cafe con Leche", author: "xyz", views: 10 },
         { subject: "coffees", author: "xyz", views: 10 },
         { subject: "coffee1", author: "xyz", views: 10 }
    ]
)

db.createCollection("users", {capped: true, size:100000})
db.users.insertMany(
    [
        { name:"David", age:45, address:"서울" },
		{ name:"DaveLee", age:25, address:"경기도" },
		{ name:"Andy", age:50, hobby:"골프", address:"경기도" },
		{ name:"Kate", age:35, address:"수원시" },
		{ name:"Brown", age:8 }
    ]
)
db.users.find()
db.users.drop()


db.users.find()

db.users.find({}, {name:1, address:1})

db.users.find({},{name:1, address:1, _id:0})

db.users.find({address:"서울"})

db.users.find({address: {$eq: "서울"}})

db.users.find({name: "DaveLee"},{name:1, age:1, address:1, _id:1})

db.users.find({name:"Kate"},{name:1, age:1, address:1})

db.users.find({age: {$gt:25}},{name:1})

db.users.find({age:{$eq:50},address:"경기도"},{name:1})

db.users.find({age:{$lt:30}}, {name:1, age:1})

db.users.find({$or: [{name:"Brown"}, {age:35}]})

db.users.find({
  name: {
    $not: {
      $eq: "Brown"
    }
  },
  age: {
    $not: {
      $eq: 45
    }
  }
})

db.users.find({
  $and: [
    {
      name: {
        $not: {
          $eq: "Brown"
        }
      }
    },
    {
      age: {
        $not: {
          $eq: 45
        }
      }
    }
  ]
})

db.users.find({
  $or: [
    {
      name: {
        $not: {
          $eq: "Brown"
        }
      }
    },
    {
      age: {
        $not: {
          $eq: 45
        }
      }
    }
  ]
})

db.users.insertMany([
   { name: "유진", age: 25, hobbies: ["독서", "영화", "요리"] },
   { name: "동현", age: 30, hobbies: ["축구", "음악", "영화"] },
   { name: "혜진", age: 35, hobbies: ["요리", "여행", "독서"] }
])

db.users.find( { hobbies: { $all: [ "축구", "음악" ] } } )

db.users.find( { hobbies: { $in: [ "축구", "요리" ] } } )

db.users.find( { hobbies: { $nin: [ "축구", "요리" ] } })

db.users.updateMany({age:{$gt:40}}, {$set:{address:"수원시"}})

db.users.find()

db.users.updateOne( { name: "유진" }, { $set: { age: 26 } } )

db.users.updateOne(
    { name: "동현" }, 
    { $set: {"name": "동현2세", age: 31, hobbies: ["축구", "음악", "영화"]}}
)

db.users.deleteMany({age:{$lte:30}})


use sample_mflix

db.movies.aggregate([
  { $match: { year: 1995 } }
])

db.movies.aggregate([
  { 
    $group: {
      _id: "$movie_id",
      commentCount: { $sum: "$runtime" }
    }
  }
])
db.movies.find().limit(5)
use sample_mflix

db.movies.aggregate([
     {
       $group: {
         _id: "$year",
         averageRating: { $avg: "$imdb.rating" }
       }
     }
   ])
 
   
db.movies.aggregate([
  {
    $group: {
         _id: "$year",
         minRating: { $min: "$imdb.rating" },
         maxRating: { $max: "$imdb.rating" }
    }
  }
])

db.movies.aggregate([
 {
   $group: {
     _id: "$year",
     titles: { $push: "$title" }
   }
 }
])

db.movies.aggregate([
  {
    $group: {
         _id: "$year",
         genres: { $addToSet: "$genres" }
    }
  }
])

db.movies.aggregate([
  {
    $project: {
      title: 1,
      // 숫자가 아닌 문자를 제거하고 숫자만 남기는 로직 (예: "1981è" -> "1981")
      cleanedYear: {
        $substrCP: [ "$year", 0, 4 ] // 대부분의 연도는 앞의 4자리이므로 앞 4글자만 추출
      }
    }
  },
  {
    $project: {
      year: { $toInt: "$cleanedYear" },
      title: 1
    }
  },
  { $sort: { "year": 1, "title": 1 } },
  {
    $group: {
      _id: "$year",
      firstMovie: { $first: "$title" },
      lastMovie: { $last: "$title" }
    }
  }
])

//2000년 이후로 출시된 영화의 수
db.movies.aggregate([
    {$match:{year:{$gt:2000}}},
    {$count: "movies_since_2000"}
])

//각 연도별로 출시된 영화의 수
db.movies.aggregate([
    { $group: { _id: "$year", totalMovies: {$sum:1} } },
    { $sort: {_id: 1} }
])

//가장 많은 영화가 출시된 연도는 언제인가요?**
db.movies.aggregate([
    { $group: { _id:"$year", total: {$sum:1} } },
    { $sort: {total: -1} },
    { $limit: 1 }
])

//**4. 각 연도별 평균 영화 러닝타임은 어떻게 되나요?**
db.movies.aggregate([
    { $group: { _id: "$year", avgRuntime: { $avg: "$runtime" } } },
    { $sort : { _id: -1 } }
])
//**5. 가장 러닝타임이 긴 영화는 어떤 영화인가요?**
db.movies.aggregate([
    { $sort: {runtimm: -1 } },
    { $limit: 1 }
])
//**6. 각 영화 장르별 평균 IMDB 평점은 어떻게 되나요?**
db.movies.aggregate([
    { $unwind: "$genres" },
    { $group: { _id: "$genres", avgRate: { $avg: "$imdb.rating" } } },
    { $sort: { avgRate: -1} }
])

//**7. 각 연도별 영화 제목의 평균 길이는 어떻게 되나요?**
db.movies.aggregate([
    { $group: { _id: "$year", avgTitleLength: { $avg: { $strLenCP: { $toString: "$title" } } } } },
    { $sort: { _id: 1 } }
])

//**8. 각 연도별로 가장 먼저 출시된 영화의 제목은 무엇인가요?**
db.movies.aggregate([
    { $sort: { "year": 1, "releaded": 1 } },
    { $group: { _id: "$year", firstMovie: { $first: "$title" } } },
    { $sort: { _id: 1 } }
])

//**9. 각 연도별로 가장 마지막에 출시된 영화의 제목은 무엇인가요?**
db.movies.aggregate([
    { $sort: { "year": 1, "released": 1 } },
    { $group: { _id: "$year", lastMovie: { $last: "$title" } } },
    { $sort: { _id: 1 } }
])

//**10. 각 연도별로 고유한 영화 장르
db.movies.aggregate([
    { $unwind: "$genres" },
    { $group: { _id: "$year", uniGenre: { $addToSet: "$genres" } } },
    { $sort: { _id: 1 } }
])



db.movies.aggregate([
    {
        $project: {
            _id: 0,
            title: 1,
            year: 1,
            titleWithYear: { $concat: ["$title", " (", { $toString: "$year" }, ")"] }
        }
    }
])

db.movies.aggregate([
    { 
        $project: { 
            title: 1,
            year: 1,
            releasedIn: { $concat: ["$title", " (", { $toString: "$year" }, ")"] }
        }
    }
])

db.comments.aggregate([
   {
      $lookup:
        {
          from: "movies",
          localField: "movie_id",
          foreignField: "_id",
          as: "movie"
        }
   }
])

db.users.aggregate([
   {
      $lookup:
        {
          from: "comments",
          localField: "email",
          foreignField: "email",
          as: "user_comments"
        }
   }
])

db.movies.aggregate([
    {
        $redact: {
            $cond: {
                if: { $gte: ["$imdb.rating", 7] },
                then: "$$KEEP",
                else: "$$PRUNE"
            }
        }
    }
])

//**1. 각 영화의 제목과 해당 영화에 달린 댓글들을 출력하세요.**
db.movies.aggregate([
    { $lookup: {
            from: "comments",
            localField: "_id",
            foreignField: "movie_id",
            as: "movie_comments"
        } },
    { $project: { _id: 0, title:1, movie_comments: {
                                         $map: {
                                             input: "$movie_comments",
                                             as: "comment",
                                             in: "$$comment.text"
                                         }
                                    }
                                }
                            },
    { $limit: 5 }
])

//**2. 평점이 가장 높은 영화의 제목과 평점을 출력하세요.**
db.movies.aggregate([
    { $match: { "imdb.rating": { $ne: "" } } },
    { $sort: { "imdb.rating": -1 } },
    { $limit: 1},
    { $project: { _id: 0, title: 1, "imdb.rating": 1 } }
])

//**3. 각 장르별로 평균 평점이 가장 높은 장르와 평균 평점을 출력하세요.**
db.movies.aggregate([
    { $unwind: "$genres"},
    { $group: { _id: "$genres", avgRate: { $avg: "$imdb.rating" } } },
    { $sort: { avgRate: -1 } },
    { $limit: 1},
    { $project: { _id: 1, avgRate: 1 } }
])

//**4. 개봉 연도별로 평균 러닝타임이 가장 짧은 영화의 개봉 연도와 평균 러닝타임을 출력하세요.**
db.movies.aggregate([
    { $group: { _id: "$year", avgRun: { $avg: "$runtime" } } },
    { $sort: { avgRun: 1 } },
    { $limit: 1},
    { $project: { _id: 0, year: "$_id", avgRun: 1 } }
])

//**5. 각 국가별로 가장 많은 영화를 제작한 감독과 그 감독의 영화 수를 출력하세요.**
db.movies.aggregate([
    { $unwind: "$directors" },
    { $unwind: "$countries" },
    { $group: { _id: {country: "$countries", director: "$directors" }, count: {$sum: 1 } } },
    { $sort: { count: -1} },
    { $group: {_id: "$_id.country", topDirector: { $first: "$_id.director"},
                                    movieCount: { $first: "$count"} } },
    { $project: { _id: 0, country: "$_id", topDirector: 1, movieCount: 1 } } 
])

//**6. 각 연도별로 가장 많은 평점을 받은 영화의 제목과 평점을 출력하세요.**
db.movies.aggregate([
    { $sort: { "year": 1, "imdb.rating": -1 } },
    { $group: {_id: "$year", title: { $first: "$title"},
                   maxRating: { $first: "$imdb.rating"} }
    },
    { $project: { _id: 0, year: "$_id", title: 1, maxRating: 1 } }
])

//**7. 각 장르별 영화 갯수를 영화 갯수가 가장 많은 순으로 출력하세요.**
db.movies.aggregate([
    { $unwind: "$genres"},
    { $group: { _id: "$genres", count: { $sum: 1 } } },
    { $sort: { "count": -1} },
    { $project: { _id: 0, genre: "$_id", movieCount: "$count"} }
])

//**8. 영화 감독별로 평균 평점이 가장 높은 감독과 그 감독의 평균 평점을 출력하세요.**
db.movies.find().limit(5) // 감독이 여러 명인 경우도 있기 때문에,배열을 풀어서 객체마다 가져올 수 있도록 unwind를 쓴다.
db.movies.aggregate([
    { $unwind: "$directors"},
    { $group: { _id: "$directors", avgRate: { $avg: "$imdb.rating" } } },
    { $sort: { avgRate: -1 } }, { $limit: 1 },
    { $project: { _id: 0, Director: "$_id", avgRating: "$avgRate" } }
])

//**9. 장르별로 평균 러닝타임이 가장 긴 장르와 그 장르의 평균 러닝타임을 출력**
db.movies.aggregate([
    { $unwind: "$genres" },
    { $group: { _id: "$genres", avgRun: { $avg: "$runtime" } } },
    { $sort: { avgRun: -1 } }, { $limit: 1 },
    { $project: { _id: 0, genre: "$_id", avgRun: 1 } }
])

//**10. 각 영화의 제목과 해당 영화에 대해 댓글을 남긴 사용자들을 출력하세요.
db.comments.find().limit(2)
db.movies.aggregate([
    { $lookup: {
        from: "comments",
        localField: "_id",
        foreignField: "movie_id",
        as: "movie_comments"
    }},
    { $project: { _id: 0, title: 1, users: "$movie_comments.name" } }
])

