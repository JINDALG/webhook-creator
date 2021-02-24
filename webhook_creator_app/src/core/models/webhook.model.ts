export interface Webhook {
  key: string;
  remaining_minutes: number;
  id: number;
  hits?: Array<any>;
}
