import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


export function showToast(type, text) {
    const settings_toast = {
        theme: "dark",
        position: "bottom-right",
        autoClose: 3000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
    }
    if (type === 'success') {
        return toast.success(text, settings_toast)
    } else if (type === 'warn') {
        return toast.warn(text, settings_toast)
    } else if (type === 'error') {
        return toast.error(text, settings_toast)
    } else if (type === 'info') {
        return toast.info(text, settings_toast)
    }
}