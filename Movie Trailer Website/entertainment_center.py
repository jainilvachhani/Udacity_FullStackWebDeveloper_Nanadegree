import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story", "Andy's favourite toy, Woody, is worried that after Andy receives his birthday gift, a new toy called Buzz Lightyear, his importance may get reduced. He thus hatches a plan to eliminate Buzz.","https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "Jake, a paraplegic marine, replaces his brother on the Na'vi inhabited Pandora for a corporate mission. He is accepted by the natives as one of their own but he must decide where his loyalties lie.","https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=azY8kmSZ2kU")

dead_poets_society = media.Movie("Dead Poets Sociey", "John Keating, a progressive English teacher, encourages his students to break free from the norms, go against the status quo and live unapologetically.","https://upload.wikimedia.org/wikipedia/en/thumb/4/49/Dead_poets_society.jpg/220px-Dead_poets_society.jpg","https://www.youtube.com/watch?v=4lj185DaZ_o")

forrest_gump = media.Movie("Forrest Gump","Forrest Gump, a man with a low I.Q., joins the army for service where he meets Dan and Bubba. However, he cannot stop thinking about his childhood sweetheart Jenny Curran, whose life is messed up.","https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg","https://www.youtube.com/watch?v=uPIEn0M8su0")

its_a_wonderful_life = media.Movie("It's A Wonderful Life","George Bailey is a small-town man whose life seems so desperate he contemplates suicide. He had always wanted to leave Bedford Falls to see the world, but circumstances and his own good heart have led him to stay. He sacrificed his education for his brother's, kept the family-run savings and loan afloat, protected the town from the avarice of the greedy banker Mr. Potter, and married his childhood sweetheart. As he prepares to jump from a bridge, his guardian angel intercedes; showing him what life would have become for the residents of Bedford Falls if he had never lived.","https://upload.wikimedia.org/wikipedia/en/thumb/9/95/Its_A_Wonderful_Life_Movie_Poster.jpg/220px-Its_A_Wonderful_Life_Movie_Poster.jpg","https://www.youtube.com/watch?v=LJfZaT8ncYk")

shawshank_redemption = media.Movie("Shawshank Redemption","Andy Dufresne, a successful banker, is arrested for the murders of his wife and her lover, and is sentenced to life imprisonment at the Shawshank prison. He becomes the most unconventional prisoner.","https://upload.wikimedia.org/wikipedia/en/thumb/8/81/ShawshankRedemptionMoviePoster.jpg/220px-ShawshankRedemptionMoviePoster.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")

battle_los_angeles = media.Movie("Battle: Los Angeles","A Marine Staff Sergeant is required to render his services again, soon after his retirement. He and his platoon must save the city from alien invaders.","https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Battle_Los_Angeles_Poster.jpg/220px-Battle_Los_Angeles_Poster.jpg","https://www.youtube.com/watch?v=Yt7ofokzn04")

act_of_valor = media.Movie("Act Of Valor","A team of U.S. Navy SEALs embark on a secret mission to rescue a kidnapped CIA operative. This leads to the discovery of a terrifying global threat which will determine the fate of the entire country.","https://upload.wikimedia.org/wikipedia/en/thumb/4/44/Act_of_Valor_poster.jpg/220px-Act_of_Valor_poster.jpg","https://www.youtube.com/watch?v=Yt7ofokzn04")

silence_of_the_lambs = media.Movie("Silence Of The Lambs","Clarice Starling, an FBI agent, seeks help from Hannibal Lecter, a psychopathic serial killer and former psychiatrist, in order to apprehend another serial killer who has been claiming female victims.","https://upload.wikimedia.org/wikipedia/en/thumb/8/86/The_Silence_of_the_Lambs_poster.jpg/220px-The_Silence_of_the_Lambs_poster.jpg","https://www.youtube.com/watch?v=ZWCAf-xLV2k")

movies = [toy_story, avatar, dead_poets_society, forrest_gump,its_a_wonderful_life,shawshank_redemption,battle_los_angeles,act_of_valor,silence_of_the_lambs]

fresh_tomatoes.open_movies_page(movies) 
