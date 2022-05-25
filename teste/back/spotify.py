# CODIGO EM NODE
#
#  var spotifyApi = new SpotifyWebApi({
#         clientId: '9404b7d0c6b54849a0c83766dd69825d',
#         clientSecret: 'fe265b4df8af4373a6026b330319f5a7'
#       });

#       var listPlaylist = []
#       spotifyApi.clientCredentialsGrant()
#         .then (function (data) {
        
#           spotifyApi.setAccessToken(data.body['access_token']);

#           spotifyApi.search(resultDeMusic, ['playlist'], { limit: 5, offset: 1 }).then(function (data) {
#             var playlist = data.body.playlists.items
            

#             var cont = 0
#             while (playlist.length != cont) {
#               var nomePlaylists = data.body.playlists.items[cont]['name']
#               listPlaylist.push(nomePlaylists)
#               cont += 1
#             }
#             console.log(listPlaylist);