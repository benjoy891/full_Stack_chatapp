import { CssBaseline, ThemeProvider, useMediaQuery } from "@mui/material";
import React, { useEffect, useMemo, useState, useCallback } from "react";
import createTheme from "../theme/theme"; 
import { ColorModeContext } from "../context/DarkModeContext";


interface ToggleColorModeProps {
    children: React.ReactNode;
}

const ToggleColorMode: React.FC<ToggleColorModeProps> = ({ children }) => {
    const prefersDarkMode = useMediaQuery("(prefers-color-scheme: dark)");
    const [mode, setMode] = useState<"light" | "dark">(
        () => (localStorage.getItem("colorMode") as "light" | "dark") || (prefersDarkMode ? "dark" : "light")
    );

    const toggleColorMode = useCallback(() => {
        setMode((prevMode) => (prevMode === "light" ? "dark" : "light"));
    }, []);

    useEffect(() => {
        localStorage.setItem("colorMode", mode);
    }, [mode]);

    const colorMode = useMemo(() => ({ toggleColorMode }), [toggleColorMode]);

    const theme = useMemo(() => createTheme(mode), [mode]);

    return (
        <ColorModeContext.Provider value={colorMode}>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                {children}
            </ThemeProvider>
        </ColorModeContext.Provider>
    );
};

export default ToggleColorMode;
