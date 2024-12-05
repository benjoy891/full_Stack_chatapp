import { Box, CssBaseline } from "@mui/material";
import PrimaryAppBar from "./PrimaryAppBar";
import PrimaryDraw from "./PrimaryDraw";
import SecondaryDraw from "./SecondaryDraw";
import Main from "./Main";
import PopularChannels from "../components/PrimaryDraw/PopularChannels";
import ExploreCategories from "../components/SecondaryDraw/ExploreCategories";
import ExploreServers from "../components/Main/ExploreServer";


const Home = () => {
    return (
        <Box sx={{ display:"flex" }}>
            <CssBaseline/>
            <PrimaryAppBar />
            <PrimaryDraw>
                <PopularChannels open={false}/>
            </PrimaryDraw>
            <SecondaryDraw>
                <ExploreCategories />
            </SecondaryDraw>
            <Main>
                <ExploreServers />
            </Main>
        </Box>
    );
};

export default Home;
