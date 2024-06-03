<template>
  <div>
    <h1>은행 찾기</h1>
    <div class="controll">
      <button @click="zoom(-1)" class="button"><span class="material-icons-in">확대</span></button>
      <button @click="zoom(1)" class="button"><span class="material-icons-out">축소</span></button>
    </div>
    <div class="map-area">
      <div class="searchbox">
        <div>
          <input class="input-text" type="text" value="" placeholder="은행을 입력하세요" @keyup.enter="searchPlace"/>
        </div>
        <div class="results">
          <div
            class="place"
            v-for="rs in sortedResults"
            :key="rs.id"
            @click="showPlace(rs)"
          >
            <h4>{{ rs.place_name }}</h4>
            <div class="addr">{{ rs.address_name }}</div>
            <div class="distance">{{ formatDistance(rs.distance) }}</div>
          </div>
        </div>
      </div>
      <div class="kmap" ref="map"></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mapInstance: null,
      centerMarker: null,
      mapOption: {
        center: {
          lat: 36.3549777,
          lng: 127.2983403,
        },
        level: 4,
      },
      search: {
        keyword: null,
        pgn: null,
        results: [],
      },
    };
  },
  computed: {
    // Calculate the distance for each result and sort them by distance
    sortedResults() {
      return this.search.results
        .map((result) => {
          const distance = this.calculateDistance(
            this.mapOption.center.lat,
            this.mapOption.center.lng,
            result.y,
            result.x
          );
          return { ...result, distance };
        })
        .sort((a, b) => a.distance - b.distance);
    },
  },
  mounted() {
    this.initializeMap();
  },
  methods: {
    initializeMap() {
      let kakao = window.kakao;
      var container = this.$refs.map;
      const { center, level } = this.mapOption;

      container.style.width = "100%";
      container.style.height = "600px";

      this.mapInstance = new kakao.maps.Map(container, {
        center: new kakao.maps.LatLng(center.lat, center.lng),
        level,
      });

      // Add a pin marker to the center coordinate
      this.centerMarker = new kakao.maps.Marker({
        position: new kakao.maps.LatLng(center.lat, center.lng),
      });

      // Display the marker on the map
      this.centerMarker.setMap(this.mapInstance);
    },
    searchPlace(e) {
  const keyword = e.target.value.trim();
  if (keyword.length === 0) {
    return;
  }
  const ps = new window.kakao.maps.services.Places();
  ps.keywordSearch(keyword, (data, status, pgn) => {
    if (status === window.kakao.maps.services.Status.OK) {
      this.search.keyword = keyword;
      this.search.pgn = pgn;
      this.search.results = data;
    } else {
      console.log('Error:', status);
    }
  });
},
    zoom(delta) {
      const level = Math.max(3, this.mapOption.level + delta);
      this.mapOption.level = level;
      this.mapInstance.setLevel(level);
    },
    showPlace(place) {
      console.log(place);
      this.mapOption.center = {
        lat: place.y,
        lng: place.x,
      };
      this.mapInstance.setCenter(
        new window.kakao.maps.LatLng(place.y, place.x)
      );

      // Move the pin marker to the new center coordinate
      this.centerMarker.setPosition(
        new kakao.maps.LatLng(place.y, place.x)
      );
    },
    calculateDistance(lat1, lng1, lat2, lng2) {
      const R = 6371; // Radius of the Earth in kilometers
      const dLat = (lat2 - lat1) * (Math.PI / 180);
      const dLng = (lng2 - lng1) * (Math.PI / 180);
      const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * (Math.PI / 180)) *
          Math.cos(lat2 * (Math.PI / 180)) *
          Math.sin(dLng / 2) *
          Math.sin(dLng / 2);
      const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
      const distance = R * c;
      return distance;
    },
    formatDistance(distance) {
      return distance.toFixed(2) + " km";
    },
  },
};
</script>

<style scoped>
.h1 {
  text-align: center;
}
.map-area {
  display: flex;
}

.searchbox {
  width: 300px;
  display: flex;
  flex-direction: column;
}

.results {
  flex: 1;
  overflow-y: auto;
}

.place {
  padding: 8px;
  cursor: pointer;
}

.place:hover {
  background-color: darkgray;
}

h4 {
  margin: 0;
}

.kmap {
  width: 100%;
  height: 600px;
}

.distance {
  color: gray;
}
.material-icons-in {
  cursor: zoom-in;
}
.material-icons-out {
  cursor: zoom-out;
}
.input-text {
  width: 200px;
  height: 30px;
  border-radius: 5px;
  color: black;
  background-color: whitesmoke;
}
 
</style>
