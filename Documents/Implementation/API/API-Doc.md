<!-- Generator: Widdershins v4.0.1 -->



<h1 id="fastapi">API Doc - v0.1.0</h1>


### Table of Contents

- [1. Default](#default)
  - [1.1. GET /](#get)
- [2. Catalog](#catalog)
  - [2.1. GET /catalog/](#get-catalog)
  - [2.2. GET /catalog/papers/search](#get-catalogpaperssearch)
  - [2.3. GET /catalog/topics/search](#get-catalogtopicssearch)
  - [2.4. GET /catalog/authors/search](#get-catalogauthorssearch)
  - [2.5. GET /catalog/same-topic](#get-catalogsame-topic)
  - [2.6. GET /catalog/co-author](#get-catalogco-author)
  - [2.7. GET /catalog/cited-tree](#get-catalogcited-tree)
- [3. Analysis](#analysis)
  - [3.1. GET /analysis/](#get-analysis)
  - [3.2. POST /analysis/upload/](#post-analysisupload)

#### Schemas

- [AuthorItemSchema](#authoritemschema)
- [AuthorResponse](#authorresponse)
- [AuthorSchema](#authorschema)
- [Body_upload_document_analysis_upload__post](#bodyupload_document_analysis_upload__post)
- [CitedConnectionItemSchema](#citedconnectionitemschema)
- [CitedTreeDataSchema](#citedtreedataschema)
- [CitedTreeResponseSchema](#citedtreeresponseschema)
- [CoAuthorConnectionItemSchema](#coauthorconnectionitemschema)
- [CoAuthorDataSchema](#coauthordataschema)
- [CoAuthorResponseSchema](#coauthorresponseschema)
- [HTTPValidationError](#httpvalidationerror)
- [PaperItemSchema](#paperitemschema)
- [PaperResponse](#paperresponse)
- [SameTopicConnectionItemSchema](#sametopicconnectionitemschema)
- [SameTopicDataSchema](#sametopicdataschema)
- [SameTopicResponseSchema](#sametopicresponseschema)
- [TopicItemSchema](#topicitemschema)
- [TopicResponse](#topicresponse)
- [TopicSchema](#topicschema)
- [ValidationError](#validationerror)

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

# Default

## GET `/`

<a id="opIdroot__get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET / \
  -H 'Accept: application/json'
```

- http
```http
GET / HTTP/1.1
Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /`

*API Root*

This is the root endpoint of the API. It serves as an initial point to check the API status and discover the base URI.

> Example responses

> 200 Response

```json
{
  "uri": "/"
}
```

> 500 Response

```json
{
  "detail": "Internal server error"
}
```

<h3 id="root__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="root__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Catalog

## GET `/catalog/`

<a id="opIdroot_catalog__get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/ \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/ HTTP/1.1
Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/catalog/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/`

*Catalog API Root*

This is the root endpoint of the Catalog API. It provides a quick check to ensure the API is operational and to discover the base URI.

> Example responses

> 200 Response

```json
{
  "uri": "/catalog"
}
```

> 500 Response

```json
{
  "detail": "Internal server error"
}
```

<h3 id="root_catalog__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="root_catalog__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## GET `/catalog/papers/search`

<a id="opIdsearch_papers_catalog_papers_search_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/papers/search \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/papers/search HTTP/1.1
Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/catalog/papers/search',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/papers/search',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/papers/search', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/papers/search', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/papers/search");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/papers/search", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/papers/search`

*Search for Papers*

Search for papers based on various filters like title, publication date, DOI, and more.

<h3 id="search_papers_catalog_papers_search_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|article_id|query|integer|false|none|
|title|query|string|false|none|
|abstract|query|string|false|none|
|publisher|query|string|false|none|
|date|query|string|false|none|
|issn|query|string|false|none|
|eissn|query|string|false|none|
|volume|query|string|false|none|
|issue|query|string|false|none|
|page|query|string|false|none|
|doi|query|string|false|none|
|meeting|query|string|false|none|
|file_path|query|string|false|none|
|type|query|string|false|none|
|container_title|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": [
    {
      "articleId": 547,
      "title": "A 1 PB/s file system to checkpoint three million MPI tasks",
      "authors": [
        {
          "authorId": 1134,
          "name": "Adam Moody"
        },
        {
          "authorId": 1136,
          "name": "Kathryn Mohror"
        },
        {
          "authorId": 1168,
          "name": "Raghunath Rajachandrasekar"
        },
        {
          "authorId": 1169,
          "name": "Dhabaleswar K. Panda"
        }
      ]
    },
    {
      "articleId": 572,
      "title": "A Large-Scale Empirical Study on Software Reuse in Mobile Apps",
      "authors": [
        {
          "authorId": 1239,
          "name": "Israel J. Mojica"
        },
        {
          "authorId": 1240,
          "name": "Bram Adams"
        },
        {
          "authorId": 1241,
          "name": "Meiyappan Nagappan"
        },
        {
          "authorId": 1242,
          "name": "Steffen Dienst"
        },
        {
          "authorId": 1243,
          "name": "Thorsten Berger"
        },
        {
          "authorId": 1244,
          "name": "Ahmed E. Hassan"
        }
      ]
    },
    {
      "articleId": 1911,
      "title": "A systematic literature review of empirical evidence on computer games and serious games",
      "authors": [
        {
          "authorId": 452,
          "name": "A. J."
        },
        {
          "authorId": 5183,
          "name": "M. Connolly"
        },
        {
          "authorId": 5184,
          "name": "Boyle Th."
        },
        {
          "authorId": 5185,
          "name": "E. A."
        },
        {
          "authorId": 5186,
          "name": "E. MacArthur"
        },
        {
          "authorId": 5187,
          "name": "Th Hainey"
        },
        {
          "authorId": 5188,
          "name": "M. Boyle"
        }
      ]
    },
    {
      "articleId": 722,
      "title": "An Empirical Analysis of Vulnerabilities in Python Packages for Web Applications",
      "authors": [
        {
          "authorId": 1642,
          "name": "J. Ruohonen"
        }
      ]
    },
    {
      "articleId": 747,
      "title": "An Empirical Comparison of Graph Databases",
      "authors": [
        {
          "authorId": 1716,
          "name": "Salim Jouili"
        },
        {
          "authorId": 1717,
          "name": "Valentin Vansteenberghe"
        }
      ]
    },
    {
      "articleId": 1702,
      "title": "An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling",
      "authors": [
        {
          "authorId": 4562,
          "name": "Vladlen Koltun"
        },
        {
          "authorId": 4563,
          "name": "J.Zico Kolter Shaojie Bai"
        }
      ]
    },
    {
      "articleId": 695,
      "title": "An empirical comparison of dependency network evolution in seven software packaging ecosystems",
      "authors": [
        {
          "authorId": 1599,
          "name": "Alexandre Decan"
        },
        {
          "authorId": 1600,
          "name": "Tom Mens"
        },
        {
          "authorId": 1602,
          "name": "Philippe Grosjean"
        }
      ]
    },
    {
      "articleId": 2297,
      "title": "An empirical examination of effective practices for teaching board game play to young children",
      "authors": [
        {
          "authorId": 6067,
          "name": "E.E. Barton"
        },
        {
          "authorId": 6068,
          "name": "E.A. Pokorski"
        },
        {
          "authorId": 6069,
          "name": "E.M. Sweeney"
        },
        {
          "authorId": 6070,
          "name": "M. Velez"
        },
        {
          "authorId": 6071,
          "name": "S. Gossett"
        },
        {
          "authorId": 6072,
          "name": "J. Qiu"
        },
        {
          "authorId": 6073,
          "name": "M. Domingo"
        }
      ]
    },
    {
      "articleId": 1467,
      "title": "An empirical study of the energy consumption of android applications",
      "authors": [
        {
          "authorId": 3938,
          "name": "Ding Li"
        },
        {
          "authorId": 3939,
          "name": "Shuai Hao"
        },
        {
          "authorId": 3940,
          "name": "Jiaping Gui"
        },
        {
          "authorId": 3941,
          "name": "William G.J. Halfond"
        }
      ]
    },
    {
      "articleId": 403,
      "title": "Becoming a vampire without being bitten: The narrative collective-assimilation hypothesis",
      "authors": [
        {
          "authorId": 754,
          "name": "S. Gabriel"
        },
        {
          "authorId": 755,
          "name": "A.F. Young"
        }
      ]
    },
    {
      "articleId": 804,
      "title": "Campus Champions",
      "authors": [
        {
          "authorId": 1850,
          "name": "X.S.E.D.E."
        }
      ]
    },
    {
      "articleId": 545,
      "title": "Coordinated Checkpoint/Restart Process Fault Tolerance for Mpi Applications on Hpc Systems",
      "authors": [
        {
          "authorId": 1163,
          "name": "Joshua Hursey"
        }
      ]
    },
    {
      "articleId": 842,
      "title": "Designing a ROCm-Aware MPI Library for AMD GPUs: Early Experiences",
      "authors": [
        {
          "authorId": 1169,
          "name": "Dhabaleswar K. Panda"
        },
        {
          "authorId": 1940,
          "name": "Kawthar Shafie Khorassani"
        },
        {
          "authorId": 1944,
          "name": "Hari Subramoni",
          "email": "subramon@cse.ohio-state.edu",
          "affiliation": "The Ohio State University Columbus"
        },
        {
          "authorId": 1977,
          "name": "Ching-Hsiang Chu"
        },
        {
          "authorId": 1979,
          "name": "Jahanzeb Hashmi"
        },
        {
          "authorId": 1980,
          "name": "Chen-Chun Chen"
        }
      ]
    },
    {
      "articleId": 1492,
      "title": "Eiciently compiling eicient query plans for modern hardware",
      "authors": [
        {
          "authorId": 4017,
          "name": "Thomas Neumann"
        }
      ]
    },
    {
      "articleId": 530,
      "title": "FTC-Charm++: an in-memory checkpoint-based fault tolerant runtime for Charm++ and MPI",
      "authors": [
        {
          "authorId": 1121,
          "name": "Gengbin Zheng"
        },
        {
          "authorId": 1122,
          "name": "Lixia Shi"
        },
        {
          "authorId": 1123,
          "name": "Laxmikant V. Kalé"
        }
      ]
    },
    {
      "articleId": 838,
      "title": "HPE CRAY MPI -SPOCK WORKSHOP",
      "authors": [
        {
          "authorId": 1975,
          "name": "O.L.C.F."
        }
      ]
    },
    {
      "articleId": 826,
      "title": "High Performance MPI over the Slingshot Interconnect: Early Experiences",
      "authors": [
        {
          "authorId": 1940,
          "name": "Kawthar Shafie Khorassani"
        },
        {
          "authorId": 1941,
          "name": "Chen Chun Chen"
        },
        {
          "authorId": 1942,
          "name": "Bharath Ramesh",
          "email": "ramesh.113@osu.edu",
          "affiliation": "The Ohio State University Columbus"
        },
        {
          "authorId": 1943,
          "name": "Aamir Shafi",
          "affiliation": "The Ohio State University Columbus"
        },
        {
          "authorId": 1944,
          "name": "Hari Subramoni",
          "email": "subramon@cse.ohio-state.edu",
          "affiliation": "The Ohio State University Columbus"
        },
        {
          "authorId": 1945,
          "name": "Dhabaleswar K Panda",
          "email": "panda@cse.ohio-state.edu",
          "affiliation": "The Ohio State University Columbus"
        }
      ]
    },
    {
      "articleId": 2314,
      "title": "Improving students' speaking performance through language board game at the eight grade of SMPIT Permata Bunda",
      "authors": [
        {
          "authorId": 6088,
          "name": "M. Sukirlan"
        },
        {
          "authorId": 6107,
          "name": "H. Hariyanto"
        },
        {
          "authorId": 6108,
          "name": "C. Sutarsyah"
        }
      ]
    },
    {
      "articleId": 2038,
      "title": "Modeling social interactions: Identification, empirical methods and policy implications",
      "authors": [
        {
          "authorId": 5423,
          "name": "W. Hartmann"
        },
        {
          "authorId": 5424,
          "name": "P. Manchanda"
        },
        {
          "authorId": 5425,
          "name": "H. Nair"
        },
        {
          "authorId": 5426,
          "name": "M. Bothner"
        },
        {
          "authorId": 5427,
          "name": "P. Dodds"
        },
        {
          "authorId": 5428,
          "name": "D. Godes"
        },
        {
          "authorId": 5429,
          "name": "K. Hosanagar"
        },
        {
          "authorId": 5430,
          "name": "C. Tucker"
        }
      ]
    },
    {
      "articleId": 832,
      "title": "OMB-GPU: A Micro-benchmark Suite for Evaluating MPI Libraries on GPU Clusters",
      "authors": [
        {
          "authorId": 1069,
          "name": "D.K. Panda"
        },
        {
          "authorId": 1946,
          "name": "D. Bureddy"
        },
        {
          "authorId": 1947,
          "name": "H. Wang"
        },
        {
          "authorId": 1948,
          "name": "A. Venkatesh"
        },
        {
          "authorId": 1949,
          "name": "S. Potluri"
        }
      ]
    },
    {
      "articleId": 625,
      "title": "On distributed memory MPI-based parallelization of SPH codes in massive HPC context",
      "authors": [
        {
          "authorId": 1408,
          "name": "G. Oger"
        },
        {
          "authorId": 1409,
          "name": "D.Le Touzé"
        },
        {
          "authorId": 1410,
          "name": "D. Guibert"
        },
        {
          "authorId": 1411,
          "name": "M. Leffe"
        },
        {
          "authorId": 1412,
          "name": "J. Biddiscombe"
        },
        {
          "authorId": 1413,
          "name": "J. Soumagne"
        },
        {
          "authorId": 1414,
          "name": "J.-G. Piccinali"
        }
      ]
    },
    {
      "articleId": 685,
      "title": "On the impact of using trivial packages: an empirical case study on npm and PyPI",
      "authors": [
        {
          "authorId": 1572,
          "name": "Rabe Abdalkareem"
        },
        {
          "authorId": 1573,
          "name": "Vinicius Oda"
        },
        {
          "authorId": 1574,
          "name": "Suhaib Mujahid"
        },
        {
          "authorId": 1575,
          "name": "Emad Shihab"
        }
      ]
    },
    {
      "articleId": 834,
      "title": "Open MPI: Goals, Concept, and Design of a Next Generation MPI Implementation",
      "authors": [
        {
          "authorId": 1291,
          "name": "Jeffrey M. Squyres"
        },
        {
          "authorId": 1292,
          "name": "George Bosilca"
        },
        {
          "authorId": 1955,
          "name": "Edgar Gabriel"
        },
        {
          "authorId": 1956,
          "name": "Graham E. Fagg"
        },
        {
          "authorId": 1957,
          "name": "Thara Angskun"
        },
        {
          "authorId": 1958,
          "name": "Jack J. Dongarra"
        },
        {
          "authorId": 1959,
          "name": "Vishal Sahay"
        },
        {
          "authorId": 1960,
          "name": "Prabhanjan Kambadur"
        },
        {
          "authorId": 1961,
          "name": "Brian Barrett"
        },
        {
          "authorId": 1962,
          "name": "Andrew Lumsdaine"
        },
        {
          "authorId": 1963,
          "name": "Ralph H. Castain"
        },
        {
          "authorId": 1964,
          "name": "David J. Daniel"
        },
        {
          "authorId": 1965,
          "name": "Richard L. Graham"
        },
        {
          "authorId": 1966,
          "name": "Timothy S. Woodall"
        }
      ]
    },
    {
      "articleId": 843,
      "title": "Optimization of Collective Communication Operations in MPICH",
      "authors": [
        {
          "authorId": 830,
          "name": "Rajeev Thakur"
        },
        {
          "authorId": 1981,
          "name": "Rolf Rabenseifner"
        },
        {
          "authorId": 1982,
          "name": "William Gropp"
        }
      ]
    },
    {
      "articleId": 1297,
      "title": "PAYJIT: Space-optimal JIT compilation and its practical implementation",
      "authors": [
        {
          "authorId": 3459,
          "name": "Jacob Brock"
        },
        {
          "authorId": 3460,
          "name": "Chen Ding"
        },
        {
          "authorId": 3461,
          "name": "Xiaoran Xu"
        },
        {
          "authorId": 3462,
          "name": "Yan Zhang"
        }
      ]
    },
    {
      "articleId": 876,
      "title": "SAT-based compilation to a non-von neumann processor",
      "authors": [
        {
          "authorId": 2077,
          "name": "Samit Chaudhuri"
        },
        {
          "authorId": 2078,
          "name": "Asmus Hetzel"
        }
      ]
    },
    {
      "articleId": 1686,
      "title": "SUNDIALS Multiphysics+MPIManyVector Performance Testing",
      "authors": [
        {
          "authorId": 4453,
          "name": "Cody J. Balos"
        },
        {
          "authorId": 4454,
          "name": "David J. Gardner"
        },
        {
          "authorId": 4455,
          "name": "Carol S. Woodward"
        },
        {
          "authorId": 4456,
          "name": "Daniel R. Reynolds"
        }
      ]
    },
    {
      "articleId": 1281,
      "title": "Subgraph frequencies: mapping the empirical and extremal geography of large graph collections",
      "authors": [
        {
          "authorId": 3040,
          "name": "Jon M. Kleinberg"
        },
        {
          "authorId": 3414,
          "name": "Johan Ugander"
        },
        {
          "authorId": 3415,
          "name": "Lars Backstrom"
        }
      ]
    },
    {
      "articleId": 484,
      "title": "Testing and Debugging Exascale Applications by Mocking MPI",
      "authors": [
        {
          "authorId": 949,
          "name": "Thomas Clune",
          "email": "thomas.l.clune@nasa.gov",
          "affiliation": "NASA Goddard Space Flight Center Greenbelt"
        },
        {
          "authorId": 950,
          "name": "Hal Finkel",
          "email": "hfinkel@anl.gov",
          "affiliation": "Leadership Computing Facility Argonne National Laboratory"
        },
        {
          "authorId": 951,
          "name": "Michael Rilee",
          "affiliation": "Rilee Systems Technologies LLC and NASA GSFC"
        }
      ]
    },
    {
      "articleId": 841,
      "title": "The MVAPICH project: Transforming research into high-performance MPI library for HPC community",
      "authors": [
        {
          "authorId": 1944,
          "name": "Hari Subramoni",
          "email": "subramon@cse.ohio-state.edu",
          "affiliation": "The Ohio State University Columbus"
        },
        {
          "authorId": 1976,
          "name": "Dhabaleswar Kumar Panda"
        },
        {
          "authorId": 1977,
          "name": "Ching-Hsiang Chu"
        },
        {
          "authorId": 1978,
          "name": "Moham-madreza Bayatpour"
        }
      ]
    },
    {
      "articleId": 377,
      "title": "Using MPI",
      "authors": [
        {
          "authorId": 699,
          "name": "W. Gropp"
        },
        {
          "authorId": 700,
          "name": "E. Lusk"
        },
        {
          "authorId": 701,
          "name": "A. Skjellum"
        }
      ]
    },
    {
      "articleId": 1713,
      "title": "What makes the diference? An empirical comparison of fusion strategies for multimodal language analysis",
      "authors": [
        {
          "authorId": 3353,
          "name": "Guansong Pang"
        },
        {
          "authorId": 4612,
          "name": "Dimitris Gkoumas"
        },
        {
          "authorId": 4613,
          "name": "C.Lioma Qiuchi Li"
        },
        {
          "authorId": 4614,
          "name": "Yijun Yu"
        }
      ]
    }
  ]
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="search_papers_catalog_papers_search_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Papers found based on the search criteria|[PaperResponse](#schemapaperresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="search_papers_catalog_papers_search_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## GET `/catalog/topics/search`

<a id="opIdsearch_topics_catalog_topics_search_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/topics/search \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/topics/search HTTP/1.1
Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/catalog/topics/search',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/topics/search',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/topics/search', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/topics/search', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/topics/search");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/topics/search", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/topics/search`

*Search for Topics*

Search for topics based on topic ID or name.

<h3 id="search_topics_catalog_topics_search_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|topic_id|query|integer|false|none|
|name|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": [
    {
      "topicId": 22,
      "topic": "method",
      "count": 1
    }
  ]
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="search_topics_catalog_topics_search_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Topics found based on the search criteria|[TopicResponse](#schematopicresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="search_topics_catalog_topics_search_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## GET `/catalog/authors/search`

<a id="opIdsearch_authors_catalog_authors_search_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/authors/search \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/authors/search HTTP/1.1
Accept: application/json
```

- javascript
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/catalog/authors/search',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/authors/search',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/authors/search', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/authors/search', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/authors/search");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/authors/search", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/authors/search`

*Search for Authors*

Search for authors based on various filters like author ID, name, email, or affiliation.

<h3 id="search_authors_catalog_authors_search_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|author_id|query|integer|false|none|
|name|query|string|false|none|
|email|query|string|false|none|
|affiliation|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": [
    {
      "authorId": 5834,
      "name": "A. TOMKINS",
      "count": 2
    },
    {
      "authorId": 5995,
      "name": "F.W. TOMPA",
      "count": 1
    },
    {
      "authorId": 2673,
      "name": "Ioan Toma",
      "count": 1
    },
    {
      "authorId": 1329,
      "name": "Kazutomo Yoshii",
      "count": 1
    },
    {
      "authorId": 4202,
      "name": "Pritom Ahmed",
      "count": 1
    },
    {
      "authorId": 2491,
      "name": "R.M. Tomasulo",
      "count": 1
    },
    {
      "authorId": 4549,
      "name": "Stanimire Tomov",
      "count": 1
    },
    {
      "authorId": 836,
      "name": "Sérgio Crisóstomo",
      "count": 1
    },
    {
      "authorId": 3722,
      "name": "Tom Bostoen",
      "count": 1
    },
    {
      "authorId": 2082,
      "name": "Tom Conte",
      "count": 1
    },
    {
      "authorId": 5064,
      "name": "Tom Gibbs",
      "count": 1
    },
    {
      "authorId": 2607,
      "name": "Tom Kenter",
      "count": 1
    },
    {
      "authorId": 1990,
      "name": "Tom Lehman",
      "count": 2
    },
    {
      "authorId": 1600,
      "name": "Tom Mens",
      "count": 2
    },
    {
      "authorId": 1279,
      "name": "Tom Peterka",
      "count": 2
    },
    {
      "authorId": 2567,
      "name": "Tom Schaul",
      "count": 1
    },
    {
      "authorId": 3584,
      "name": "Tom W. Keller",
      "count": 1
    },
    {
      "authorId": 4101,
      "name": "Tomas Karnagel",
      "count": 1
    },
    {
      "authorId": 5114,
      "name": "Tommaso Calarco",
      "count": 1
    },
    {
      "authorId": 5129,
      "name": "Tommer Leyvand",
      "count": 1
    },
    {
      "authorId": 4318,
      "name": "Tomoharu Iwata",
      "count": 1
    },
    {
      "authorId": 558,
      "name": "a n tomera",
      "count": 1
    }
  ]
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="search_authors_catalog_authors_search_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Authors found based on the search criteria|[AuthorResponse](#schemaauthorresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="search_authors_catalog_authors_search_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## GET `/catalog/same-topic`

<a id="opIdget_same_topic_catalog_same_topic_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/same-topic \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/same-topic HTTP/1.1
Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/catalog/same-topic',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/same-topic',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/same-topic', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/same-topic', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/same-topic");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/same-topic", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/same-topic`

*Articles under the Same Topic*

Retrieve articles that are related to the same topic based on a comprehensive set of article filters.

<h3 id="get_same_topic_catalog_same_topic_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|article_id|query|integer|false|none|
|title|query|string|false|none|
|abstract|query|string|false|none|
|publisher|query|string|false|none|
|date|query|string|false|none|
|issn|query|string|false|none|
|eissn|query|string|false|none|
|volume|query|string|false|none|
|issue|query|string|false|none|
|page|query|string|false|none|
|doi|query|string|false|none|
|meeting|query|string|false|none|
|file_path|query|string|false|none|
|type|query|string|false|none|
|container_title|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": {
    "connections": [
      {
        "topic": 11,
        "papers": [
          53,
          98
        ]
      },
      {
        "topic": 19,
        "papers": [
          98
        ]
      },
      {
        "topic": 20,
        "papers": [
          98
        ]
      },
      {
        "topic": 21,
        "papers": [
          98
        ]
      },
      {
        "topic": 22,
        "papers": [
          98
        ]
      },
      {
        "topic": 23,
        "papers": [
          98
        ]
      },
      {
        "topic": 24,
        "papers": [
          98
        ]
      },
      {
        "topic": 25,
        "papers": [
          98
        ]
      },
      {
        "topic": 26,
        "papers": [
          98
        ]
      }
    ],
    "topics": [
      {
        "topicId": 11,
        "name": "operator"
      },
      {
        "topicId": 19,
        "name": "partition"
      },
      {
        "topicId": 20,
        "name": "fuzzy"
      },
      {
        "topicId": 21,
        "name": "relation"
      },
      {
        "topicId": 22,
        "name": "method"
      },
      {
        "topicId": 23,
        "name": "order"
      },
      {
        "topicId": 24,
        "name": "convex"
      },
      {
        "topicId": 25,
        "name": "total"
      },
      {
        "topicId": 26,
        "name": "address"
      }
    ],
    "papers": [
      {
        "articleId": 98,
        "title": "A method for deriving order compatible fuzzy relations from convex fuzzy partitions",
        "authors": [
          {
            "authorId": 219,
            "name": "Sandra Sandri",
            "email": "sandra.sandri@inpe.br",
            "affiliation": "Brazilian National Institute for Space Research (INPE)"
          },
          {
            "authorId": 220,
            "name": "Flávia Toledo Martins-Bedê",
            "affiliation": "Brazilian National Institute for Space Research (INPE)"
          }
        ]
      },
      {
        "articleId": 53,
        "title": "Development of child's home environment indexes based on consistent families of aggregation operators with prioritized hierarchical information",
        "authors": [
          {
            "authorId": 135,
            "name": "Karina Rojas",
            "email": "krojas@spm.uach.cl",
            "affiliation": "Facultad de Ciencias Matemáticas"
          },
          {
            "authorId": 136,
            "name": "Daniel Gómez",
            "email": "dagomez@estad.ucm.es",
            "affiliation": "Escuela de Estadística"
          },
          {
            "authorId": 137,
            "name": "Javier Montero",
            "affiliation": "Facultad de Ciencias Matemáticas"
          },
          {
            "authorId": 138,
            "name": "J Tinguaro Rodríguez",
            "affiliation": "Facultad de Ciencias Matemáticas"
          },
          {
            "authorId": 139,
            "name": "Andrea Valdivia",
            "email": "andrea.valdivia@uchile.cl",
            "affiliation": "Instituto de Comunicación e Imagen"
          },
          {
            "authorId": 140,
            "name": "Francisco Paiva",
            "email": "fpaiva@uach.cl",
            "affiliation": "Facultad de Filosofía y Humanidades"
          }
        ]
      }
    ]
  }
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="get_same_topic_catalog_same_topic_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Articles found based on the search criteria|[SameTopicResponseSchema](#schemasametopicresponseschema)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="get_same_topic_catalog_same_topic_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## GET `/catalog/co-author`

<a id="opIdget_co_author_by_filter_catalog_co_author_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/co-author \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/co-author HTTP/1.1
Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/catalog/co-author',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/co-author',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/co-author', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/co-author', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/co-author");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/co-author", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/co-author`

*Co-authorship Information*

Retrieve co-authorship information based on an article's filter.

<h3 id="get_co_author_by_filter_catalog_co_author_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|article_id|query|integer|false|none|
|title|query|string|false|none|
|abstract|query|string|false|none|
|publisher|query|string|false|none|
|date|query|string|false|none|
|issn|query|string|false|none|
|eissn|query|string|false|none|
|volume|query|string|false|none|
|issue|query|string|false|none|
|page|query|string|false|none|
|doi|query|string|false|none|
|meeting|query|string|false|none|
|file_path|query|string|false|none|
|type|query|string|false|none|
|container_title|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": {
    "connections": [
      {
        "author": 21,
        "papers": [
          9
        ]
      },
      {
        "author": 22,
        "papers": [
          9,
          13,
          14,
          15
        ]
      },
      {
        "author": 23,
        "papers": [
          9
        ]
      },
      {
        "author": 24,
        "papers": [
          9
        ]
      }
    ],
    "authors": [
      {
        "authorId": 22,
        "name": "H. Gasteiger"
      }
    ],
    "papers": [
      {
        "articleId": 9,
        "title": "ZahlenZauberei",
        "authors": [
          {
            "authorId": 21,
            "name": "R. Dolenc"
          },
          {
            "authorId": 22,
            "name": "H. Gasteiger"
          },
          {
            "authorId": 23,
            "name": "G. Kraft"
          },
          {
            "authorId": 24,
            "name": "G. Loibl"
          }
        ]
      },
      {
        "articleId": 13,
        "title": "Elementare mathematische Bildung im Alltag der Kindertagesstätte: Grundlegung und Evaluation eines kompetenzorientierten Förderansatzes",
        "authors": [
          {
            "authorId": 22,
            "name": "H. Gasteiger"
          }
        ]
      },
      {
        "articleId": 14,
        "title": "Fostering early mathematical competencies in natural learning situations-Foundation and challenges of a competence-oriented concept of mathematics education in kindergarten",
        "authors": [
          {
            "authorId": 22,
            "name": "H. Gasteiger"
          }
        ]
      },
      {
        "articleId": 15,
        "title": "Professionalization of early childhood educators with a focus on natural learning situations and individual development of mathematical competencies: Results from an evaluation study",
        "authors": [
          {
            "authorId": 22,
            "name": "H. Gasteiger"
          }
        ]
      }
    ]
  }
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="get_co_author_by_filter_catalog_co_author_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Co-authorship information found based on the search criteria|[CoAuthorResponseSchema](#schemacoauthorresponseschema)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="get_co_author_by_filter_catalog_co_author_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## GET `/catalog/cited-tree`

<a id="opIdget_cited_tree_by_filter_catalog_cited_tree_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/cited-tree \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/cited-tree HTTP/1.1
Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/catalog/cited-tree',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/cited-tree',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/cited-tree', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/cited-tree', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/cited-tree");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/cited-tree", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/cited-tree`

*Cited Tree of an Article*

Retrieve the citation tree of an article based on an article's filter.

<h3 id="get_cited_tree_by_filter_catalog_cited_tree_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|article_id|query|integer|false|none|
|title|query|string|false|none|
|abstract|query|string|false|none|
|publisher|query|string|false|none|
|date|query|string|false|none|
|issn|query|string|false|none|
|eissn|query|string|false|none|
|volume|query|string|false|none|
|issue|query|string|false|none|
|page|query|string|false|none|
|doi|query|string|false|none|
|meeting|query|string|false|none|
|file_path|query|string|false|none|
|type|query|string|false|none|
|container_title|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": {
    "connections": [
      {
        "fromPaper": 98,
        "toPaper": [
          75,
          99,
          100,
          101,
          102,
          103,
          104,
          105,
          106,
          107,
          108,
          109,
          110,
          111,
          112,
          113,
          114,
          115,
          116,
          117,
          118,
          119,
          120,
          121,
          122,
          123,
          124,
          125,
          126,
          127
        ]
      }
    ],
    "papers": [
      {
        "articleId": 75,
        "title": "A coloring algorithm for image classification, Inf",
        "authors": [
          {
            "authorId": 142,
            "name": "J. Montero"
          },
          {
            "authorId": 169,
            "name": "R. Mesiar"
          },
          {
            "authorId": 188,
            "name": "D. Gómez"
          },
          {
            "authorId": 189,
            "name": "J. Yáñez"
          },
          {
            "authorId": 229,
            "name": "B. Baets"
          },
          {
            "authorId": 230,
            "name": "T.-partitions"
          }
        ]
      },
      {
        "articleId": 98,
        "title": "A method for deriving order compatible fuzzy relations from convex fuzzy partitions",
        "authors": [
          {
            "authorId": 219,
            "name": "Sandra Sandri",
            "email": "sandra.sandri@inpe.br",
            "affiliation": "Brazilian National Institute for Space Research (INPE)"
          },
          {
            "authorId": 220,
            "name": "Flávia Toledo Martins-Bedê",
            "affiliation": "Brazilian National Institute for Space Research (INPE)"
          }
        ]
      },
      {
        "articleId": 99,
        "title": "On learning similarity relations in fuzzy case-based reasoning",
        "authors": [
          {
            "authorId": 221,
            "name": "E. Armengol"
          },
          {
            "authorId": 222,
            "name": "F. Esteva"
          },
          {
            "authorId": 223,
            "name": "L. Godo"
          },
          {
            "authorId": 224,
            "name": "V. Torra"
          }
        ]
      },
      {
        "articleId": 100,
        "title": "Pattern Recognition with Fuzzy Objective Function Algorithms",
        "authors": [
          {
            "authorId": 225,
            "name": "J.C. Bezdek"
          }
        ]
      },
      {
        "articleId": 101,
        "title": "Fuzzy tolerance relation, fuzzy tolerance space and basis",
        "authors": [
          {
            "authorId": 226,
            "name": "M. Das"
          },
          {
            "authorId": 227,
            "name": "M.K. Chakraborty"
          },
          {
            "authorId": 228,
            "name": "T.K. Ghoshal"
          }
        ]
      },
      {
        "articleId": 102,
        "title": "On (un)suitable fuzzy relations to model approximate equality",
        "authors": [
          {
            "authorId": 231,
            "name": "M. Cock"
          },
          {
            "authorId": 232,
            "name": "E. Kerre"
          }
        ]
      },
      {
        "articleId": 103,
        "title": "Pseudometrics and fuzzy relations",
        "authors": [
          {
            "authorId": 233,
            "name": "J. Dobrakovová"
          }
        ]
      },
      {
        "articleId": 104,
        "title": "Restoring consistency in systems of fuzzy gradual rules using similarity relations",
        "authors": [
          {
            "authorId": 223,
            "name": "L. Godo"
          },
          {
            "authorId": 234,
            "name": "I. Drummond"
          },
          {
            "authorId": 235,
            "name": "S. Sandri"
          }
        ]
      },
      {
        "articleId": 105,
        "title": "Making fuzzy absolute and fuzzy relative orders of magnitude consistent",
        "authors": [
          {
            "authorId": 236,
            "name": "D. Dubois"
          },
          {
            "authorId": 237,
            "name": "A. Hadjali"
          },
          {
            "authorId": 238,
            "name": "H. Prade"
          }
        ]
      },
      {
        "articleId": 106,
        "title": "Learning fuzzy systems with similarity relations",
        "authors": [
          {
            "authorId": 223,
            "name": "L. Godo"
          },
          {
            "authorId": 234,
            "name": "I. Drummond"
          },
          {
            "authorId": 235,
            "name": "S. Sandri"
          }
        ]
      },
      {
        "articleId": 107,
        "title": "Case-based reasoning retrieval and reuse using case resemblance hypergraphs",
        "authors": [
          {
            "authorId": 234,
            "name": "I. Drummond"
          },
          {
            "authorId": 235,
            "name": "S. Sandri"
          },
          {
            "authorId": 239,
            "name": "T. Fanoiki"
          }
        ]
      },
      {
        "articleId": 108,
        "title": "A similarity-based approach to deal with inconsistency in systems of fuzzy gradual rules",
        "authors": [
          {
            "authorId": 223,
            "name": "L. Godo"
          },
          {
            "authorId": 235,
            "name": "S. Sandri"
          }
        ]
      },
      {
        "articleId": 109,
        "title": "Resemblance is a nearness, Fuzzy Sets Syst",
        "authors": [
          {
            "authorId": 240,
            "name": "V. Janis"
          }
        ]
      },
      {
        "articleId": 110,
        "title": "I-fuzzy relations and I-fuzzy partitions, Inf",
        "authors": [
          {
            "authorId": 169,
            "name": "R. Mesiar"
          },
          {
            "authorId": 241,
            "name": "B. Jayaram"
          }
        ]
      },
      {
        "articleId": 111,
        "title": "Practical inference with systems of gradual implicative rules",
        "authors": [
          {
            "authorId": 236,
            "name": "D. Dubois"
          },
          {
            "authorId": 242,
            "name": "H. Jones"
          },
          {
            "authorId": 243,
            "name": "B. Charnomordic"
          },
          {
            "authorId": 244,
            "name": "S. Guillaume"
          }
        ]
      },
      {
        "articleId": 112,
        "title": "New results in fuzzy clustering based on the concept of indistinguishability relations",
        "authors": [
          {
            "authorId": 245,
            "name": "R.Lopez Mantaras"
          },
          {
            "authorId": 246,
            "name": "L. Valverde"
          }
        ]
      },
      {
        "articleId": 113,
        "title": "Semi-orders and a theory of utility discrimination",
        "authors": [
          {
            "authorId": 204,
            "name": "R.D. Luce"
          }
        ]
      },
      {
        "articleId": 114,
        "title": "Classification of schistosomiasis prevalence using fuzzy case-based reasoning",
        "authors": [
          {
            "authorId": 223,
            "name": "L. Godo"
          },
          {
            "authorId": 235,
            "name": "S. Sandri"
          },
          {
            "authorId": 247,
            "name": "F.T. Martins-Bedê"
          },
          {
            "authorId": 248,
            "name": "L.V. Dutra"
          },
          {
            "authorId": 249,
            "name": "C. Freitas"
          },
          {
            "authorId": 250,
            "name": "O.S. Carvalho"
          },
          {
            "authorId": 251,
            "name": "R.J.P.S. Guimares"
          },
          {
            "authorId": 252,
            "name": "R.S. Amaral"
          }
        ]
      },
      {
        "articleId": 115,
        "title": "Aggregation of monotone reciprocal relations with application to group decision making",
        "authors": [
          {
            "authorId": 229,
            "name": "B. Baets"
          },
          {
            "authorId": 253,
            "name": "M. Rademaker"
          }
        ]
      },
      {
        "articleId": 116,
        "title": "Indistinguishability Operators, Modelling Fuzzy Equalities and Fuzzy Equivalence Relations",
        "authors": [
          {
            "authorId": 254,
            "name": "J. Recasens"
          }
        ]
      },
      {
        "articleId": 117,
        "title": "A new approach to clustering, Inf",
        "authors": [
          {
            "authorId": 255,
            "name": "R. Ruspini"
          }
        ]
      },
      {
        "articleId": 118,
        "title": "Order compatible fuzzy relations and their elicitation from general fuzzy partitions",
        "authors": [
          {
            "authorId": 235,
            "name": "S. Sandri"
          },
          {
            "authorId": 247,
            "name": "F.T. Martins-Bedê"
          }
        ]
      },
      {
        "articleId": 119,
        "title": "A generalized definition of rough approximations based on similarity",
        "authors": [
          {
            "authorId": 256,
            "name": "R. Slowinski"
          },
          {
            "authorId": 257,
            "name": "D. Vanderpooten"
          }
        ]
      },
      {
        "articleId": 120,
        "title": "Searching for flexible repeated patterns using a non-transitive similarity relation",
        "authors": [
          {
            "authorId": 258,
            "name": "H. Soldano"
          },
          {
            "authorId": 259,
            "name": "A. Viari"
          },
          {
            "authorId": 260,
            "name": "M. Champesme"
          }
        ]
      },
      {
        "articleId": 121,
        "title": "Modelling a linguistic variable as a hierarchical family of partitions induced by an indistinguishability operator",
        "authors": [
          {
            "authorId": 254,
            "name": "J. Recasens"
          },
          {
            "authorId": 261,
            "name": "A. Soto"
          }
        ]
      },
      {
        "articleId": 122,
        "title": "A characterization of arbitrary Ruspini partitions by fuzzy similarity relations",
        "authors": [
          {
            "authorId": 262,
            "name": "H. Thiele"
          }
        ]
      },
      {
        "articleId": 123,
        "title": "On the learning of weights in some aggregation operators: the weighted mean and owa operators",
        "authors": [
          {
            "authorId": 224,
            "name": "V. Torra"
          }
        ]
      },
      {
        "articleId": 124,
        "title": "Learning weights for the quasi-weighted means",
        "authors": [
          {
            "authorId": 224,
            "name": "V. Torra"
          }
        ]
      },
      {
        "articleId": 125,
        "title": "Features of similarity",
        "authors": [
          {
            "authorId": 263,
            "name": "A. Tversky"
          }
        ]
      },
      {
        "articleId": 126,
        "title": "On the structure of F-indistinguishability operators",
        "authors": [
          {
            "authorId": 246,
            "name": "L. Valverde"
          }
        ]
      },
      {
        "articleId": 127,
        "title": "Similarity relations and fuzzy orderings, Inf",
        "authors": [
          {
            "authorId": 264,
            "name": "L. Zadeh"
          }
        ]
      }
    ]
  }
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="get_cited_tree_by_filter_catalog_cited_tree_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Cited tree found based on the search criteria|[CitedTreeResponseSchema](#schemacitedtreeresponseschema)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="get_cited_tree_by_filter_catalog_cited_tree_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Analysis

## GET `/analysis/`

<a id="opIdroot_analysis__get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /analysis/ \
  -H 'Accept: application/json'
```

- http
```http
GET /analysis/ HTTP/1.1
Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/analysis/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/analysis/',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/analysis/', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/analysis/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/analysis/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/analysis/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /analysis/`

*Analysis API Root*

This is the root endpoint of the Analysis API. It can be used to check if the API is up and running.

> Example responses

> 200 Response

```json
{
  "uri": "/analysis"
}
```

> 500 Response

```json
{
  "detail": "Internal server error"
}
```

<h3 id="root_analysis__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="root_analysis__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## POST `/analysis/upload/`

<a id="opIdupload_document_analysis_upload__post"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X POST /analysis/upload/ \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json'
```

- http
```http
POST /analysis/upload/ HTTP/1.1
Content-Type: multipart/form-data
Accept: application/json
```

- javascript
```javascript
const inputBody = '{
  "file": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json'
};

fetch('/analysis/upload/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

result = RestClient.post '/analysis/upload/',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('/analysis/upload/', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/analysis/upload/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/analysis/upload/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/analysis/upload/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`POST /analysis/upload/`

*Upload a document*

Upload a document to the server and process it. The document will be saved, analyzed, and the extracted information will be stored.

> Body parameter

```yaml
file: string

```

<h3 id="upload_document_analysis_upload__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|any|true|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "message": "File uploaded successfully",
  "data": {
    "title": "Example Title",
    "authors": [
      {
        "name": "Author One",
        "affiliation": "University of Examples"
      }
    ],
    "abstract": "This is an example of an abstract from the uploaded document.",
    "keywords": [
      "example",
      "document",
      "upload"
    ]
  }
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "detail": "Could not save file"
}
```

<h3 id="upload_document_analysis_upload__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Document uploaded and processed successfully.|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="upload_document_analysis_upload__post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_AuthorItemSchema">AuthorItemSchema</h2>
<!-- backwards compatibility -->
<a id="schemaauthoritemschema"></a>
<a id="schema_AuthorItemSchema"></a>
<a id="tocSauthoritemschema"></a>
<a id="tocsauthoritemschema"></a>

```json
{
  "authorId": 0,
  "name": "string",
  "count": 0
}

```

AuthorItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|authorId|integer|false|none|The unique identifier of the author.|
|name|string|false|none|The name of the author.|
|count|integer|false|none|The number of papers by the author.|

<h2 id="tocS_AuthorResponse">AuthorResponse</h2>
<!-- backwards compatibility -->
<a id="schemaauthorresponse"></a>
<a id="schema_AuthorResponse"></a>
<a id="tocSauthorresponse"></a>
<a id="tocsauthorresponse"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": []
}

```

AuthorResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[[AuthorItemSchema](#schemaauthoritemschema)]|false|none|The list of authors.|

<h2 id="tocS_AuthorSchema">AuthorSchema</h2>
<!-- backwards compatibility -->
<a id="schemaauthorschema"></a>
<a id="schema_AuthorSchema"></a>
<a id="tocSauthorschema"></a>
<a id="tocsauthorschema"></a>

```json
{
  "authorId": 0,
  "name": "string",
  "email": "string",
  "affiliation": "string"
}

```

AuthorSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|authorId|integer|false|none|The unique identifier of the author.|
|name|string|false|none|The name of the author.|
|email|string|false|none|The email of the author.|
|affiliation|string|false|none|The affiliation of the author.|

<h2 id="tocS_Body_upload_document_analysis_upload__post">Body_upload_document_analysis_upload__post</h2>
<!-- backwards compatibility -->
<a id="schemabody_upload_document_analysis_upload__post"></a>
<a id="schema_Body_upload_document_analysis_upload__post"></a>
<a id="tocSbody_upload_document_analysis_upload__post"></a>
<a id="tocsbody_upload_document_analysis_upload__post"></a>

```json
{
  "file": "string"
}

```

Body_upload_document_analysis_upload__post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|file|string(binary)|true|none|The document file to be uploaded.|

<h2 id="tocS_CitedConnectionItemSchema">CitedConnectionItemSchema</h2>
<!-- backwards compatibility -->
<a id="schemacitedconnectionitemschema"></a>
<a id="schema_CitedConnectionItemSchema"></a>
<a id="tocScitedconnectionitemschema"></a>
<a id="tocscitedconnectionitemschema"></a>

```json
{
  "fromPaper": 0,
  "toPaper": []
}

```

CitedConnectionItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|fromPaper|integer|true|none|The unique identifier of the paper.|
|toPaper|[integer]|false|none|The list of papers cited by the from paper.|

<h2 id="tocS_CitedTreeDataSchema">CitedTreeDataSchema</h2>
<!-- backwards compatibility -->
<a id="schemacitedtreedataschema"></a>
<a id="schema_CitedTreeDataSchema"></a>
<a id="tocScitedtreedataschema"></a>
<a id="tocscitedtreedataschema"></a>

```json
{
  "connections": [],
  "papers": []
}

```

CitedTreeDataSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|connections|[[CitedConnectionItemSchema](#schemacitedconnectionitemschema)]|false|none|The list of connections.|
|papers|[[PaperItemSchema](#schemapaperitemschema)]|false|none|The list of papers.|

<h2 id="tocS_CitedTreeResponseSchema">CitedTreeResponseSchema</h2>
<!-- backwards compatibility -->
<a id="schemacitedtreeresponseschema"></a>
<a id="schema_CitedTreeResponseSchema"></a>
<a id="tocScitedtreeresponseschema"></a>
<a id="tocscitedtreeresponseschema"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": {}
}

```

CitedTreeResponseSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[CitedTreeDataSchema](#schemacitedtreedataschema)|false|none|The data of the response.|

<h2 id="tocS_CoAuthorConnectionItemSchema">CoAuthorConnectionItemSchema</h2>
<!-- backwards compatibility -->
<a id="schemacoauthorconnectionitemschema"></a>
<a id="schema_CoAuthorConnectionItemSchema"></a>
<a id="tocScoauthorconnectionitemschema"></a>
<a id="tocscoauthorconnectionitemschema"></a>

```json
{
  "author": 0,
  "papers": []
}

```

CoAuthorConnectionItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|author|integer|false|none|The unique identifier of the author.|
|papers|[integer]|false|none|The list of papers by the author.|

<h2 id="tocS_CoAuthorDataSchema">CoAuthorDataSchema</h2>
<!-- backwards compatibility -->
<a id="schemacoauthordataschema"></a>
<a id="schema_CoAuthorDataSchema"></a>
<a id="tocScoauthordataschema"></a>
<a id="tocscoauthordataschema"></a>

```json
{
  "connections": [],
  "authors": [],
  "papers": []
}

```

CoAuthorDataSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|connections|[[CoAuthorConnectionItemSchema](#schemacoauthorconnectionitemschema)]|false|none|The list of connections.|
|authors|[[AuthorSchema](#schemaauthorschema)]|false|none|The list of authors.|
|papers|[[PaperItemSchema](#schemapaperitemschema)]|false|none|The list of papers.|

<h2 id="tocS_CoAuthorResponseSchema">CoAuthorResponseSchema</h2>
<!-- backwards compatibility -->
<a id="schemacoauthorresponseschema"></a>
<a id="schema_CoAuthorResponseSchema"></a>
<a id="tocScoauthorresponseschema"></a>
<a id="tocscoauthorresponseschema"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": {}
}

```

CoAuthorResponseSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[CoAuthorDataSchema](#schemacoauthordataschema)|false|none|The data of the response.|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_PaperItemSchema">PaperItemSchema</h2>
<!-- backwards compatibility -->
<a id="schemapaperitemschema"></a>
<a id="schema_PaperItemSchema"></a>
<a id="tocSpaperitemschema"></a>
<a id="tocspaperitemschema"></a>

```json
{
  "articleId": 0,
  "title": "string",
  "authors": []
}

```

PaperItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|articleId|integer|false|none|The unique identifier of the paper.|
|title|string|false|none|The title of the paper.|
|authors|[[AuthorSchema](#schemaauthorschema)]|false|none|The authors of the paper.|

<h2 id="tocS_PaperResponse">PaperResponse</h2>
<!-- backwards compatibility -->
<a id="schemapaperresponse"></a>
<a id="schema_PaperResponse"></a>
<a id="tocSpaperresponse"></a>
<a id="tocspaperresponse"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": []
}

```

PaperResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[[PaperItemSchema](#schemapaperitemschema)]|false|none|The list of papers.|

<h2 id="tocS_SameTopicConnectionItemSchema">SameTopicConnectionItemSchema</h2>
<!-- backwards compatibility -->
<a id="schemasametopicconnectionitemschema"></a>
<a id="schema_SameTopicConnectionItemSchema"></a>
<a id="tocSsametopicconnectionitemschema"></a>
<a id="tocssametopicconnectionitemschema"></a>

```json
{
  "topic": 0,
  "papers": []
}

```

SameTopicConnectionItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|topic|integer|false|none|The unique identifier of the topic.|
|papers|[integer]|false|none|The list of papers in the topic.|

<h2 id="tocS_SameTopicDataSchema">SameTopicDataSchema</h2>
<!-- backwards compatibility -->
<a id="schemasametopicdataschema"></a>
<a id="schema_SameTopicDataSchema"></a>
<a id="tocSsametopicdataschema"></a>
<a id="tocssametopicdataschema"></a>

```json
{
  "connections": [],
  "topics": [],
  "papers": []
}

```

SameTopicDataSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|connections|[[SameTopicConnectionItemSchema](#schemasametopicconnectionitemschema)]|false|none|The list of connections.|
|topics|[[TopicSchema](#schematopicschema)]|false|none|The list of topics.|
|papers|[[PaperItemSchema](#schemapaperitemschema)]|false|none|The list of papers.|

<h2 id="tocS_SameTopicResponseSchema">SameTopicResponseSchema</h2>
<!-- backwards compatibility -->
<a id="schemasametopicresponseschema"></a>
<a id="schema_SameTopicResponseSchema"></a>
<a id="tocSsametopicresponseschema"></a>
<a id="tocssametopicresponseschema"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": {}
}

```

SameTopicResponseSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[SameTopicDataSchema](#schemasametopicdataschema)|false|none|The data of the response.|

<h2 id="tocS_TopicItemSchema">TopicItemSchema</h2>
<!-- backwards compatibility -->
<a id="schematopicitemschema"></a>
<a id="schema_TopicItemSchema"></a>
<a id="tocStopicitemschema"></a>
<a id="tocstopicitemschema"></a>

```json
{
  "topicId": 0,
  "topic": "string",
  "count": 0
}

```

TopicItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|topicId|integer|false|none|The unique identifier of the topic.|
|topic|string|false|none|The name of the topic.|
|count|integer|false|none|The number of papers in the topic.|

<h2 id="tocS_TopicResponse">TopicResponse</h2>
<!-- backwards compatibility -->
<a id="schematopicresponse"></a>
<a id="schema_TopicResponse"></a>
<a id="tocStopicresponse"></a>
<a id="tocstopicresponse"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": []
}

```

TopicResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[[TopicItemSchema](#schematopicitemschema)]|false|none|The list of topics.|

<h2 id="tocS_TopicSchema">TopicSchema</h2>
<!-- backwards compatibility -->
<a id="schematopicschema"></a>
<a id="schema_TopicSchema"></a>
<a id="tocStopicschema"></a>
<a id="tocstopicschema"></a>

```json
{
  "topicId": 0,
  "name": "string"
}

```

TopicSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|topicId|integer|false|none|The unique identifier of the topic.|
|name|string|false|none|The name of the topic.|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|
