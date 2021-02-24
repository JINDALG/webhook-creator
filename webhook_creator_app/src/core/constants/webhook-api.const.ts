import { environment } from 'src/environments/environment';

export const WEBHOOK_LIST_API = `${environment.API_BASE_URL}hooks/`;
export const WEBHOOK_CREATE_API = WEBHOOK_LIST_API;
export const WEBHOOK_DETAIL_API = (webhookId: number) =>
  `${environment.API_BASE_URL}hooks/${webhookId}/`;
